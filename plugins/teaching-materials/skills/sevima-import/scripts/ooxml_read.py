"""Read the parts of an .xlsx template that filling it depends on: sheet location, shared strings, header row."""

import posixpath
import re
import xml.etree.ElementTree as ET

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"m": MAIN}
WORKBOOK = "xl/workbook.xml"
WORKBOOK_RELS = "xl/_rels/workbook.xml.rels"
SHARED_STRINGS = "xl/sharedStrings.xml"
ROW_PATTERN = r'<row r="%d"(?P<attrs>[^>]*?)(?:/>|>(?P<cells>.*?)</row>)'


class TemplateError(Exception):
    pass


def sheet_path(package, sheet_name):
    sheets = ET.fromstring(package.read(WORKBOOK)).findall("m:sheets/m:sheet", NS)
    if sheet_name is None:
        chosen = sheets[0]
    else:
        chosen = next((sheet for sheet in sheets if sheet.get("name") == sheet_name), None)
    if chosen is None:
        names = ", ".join(sheet.get("name") for sheet in sheets)
        raise TemplateError("sheet %r not found; the template has: %s" % (sheet_name, names))
    rel_id = chosen.get("{%s}id" % REL)
    relations = ET.fromstring(package.read(WORKBOOK_RELS))
    target = next(rel.get("Target") for rel in relations if rel.get("Id") == rel_id)
    if target.startswith("/"):
        return chosen.get("name"), target.lstrip("/")
    return chosen.get("name"), posixpath.normpath(posixpath.join("xl", target))


def shared_strings(package):
    if SHARED_STRINGS not in package.namelist():
        raise TemplateError("the template has no shared-strings table; re-download it from Edlink")
    root = ET.fromstring(package.read(SHARED_STRINGS))
    return ["".join(node.text or "" for node in item.iter("{%s}t" % MAIN))
            for item in root.findall("m:si", NS)]


def template_row(sheet_xml, number):
    match = re.search(ROW_PATTERN % number, sheet_xml, re.DOTALL)
    if match is None:
        return None, []
    cells = re.findall(r'<c r="([A-Z]+)%d"([^>]*?)(?:/>|>(.*?)</c>)' % number, match.group("cells") or "",
                       re.DOTALL)
    return match, cells


def header_columns(sheet_xml, strings):
    match, cells = template_row(sheet_xml, 1)
    if match is None:
        raise TemplateError("the template sheet has no header row")
    header = []
    for column, attrs, body in cells:
        value = re.search(r"<v>(.*?)</v>", body or "")
        text = ""
        if value and 't="s"' in attrs:
            text = strings[int(value.group(1))]
        elif value:
            text = value.group(1)
        header.append((column, text.strip()))
    while header and not header[-1][1]:
        header.pop()
    return header


def data_row_format(sheet_xml):
    match, cells = template_row(sheet_xml, 2)
    if match is None:
        match, cells = template_row(sheet_xml, 1)
    styles = {column: re.search(r's="\d+"', attrs) for column, attrs, _ in cells}
    return match.group("attrs"), {column: found.group(0) for column, found in styles.items() if found}
