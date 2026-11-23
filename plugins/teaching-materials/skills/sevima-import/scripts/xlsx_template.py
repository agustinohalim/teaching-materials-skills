"""Write rows into a copy of an Edlink import template, keeping the template's own package intact.

Edlink's templates store text in a shared-strings table. A workbook rebuilt from scratch by a library that
writes inline strings imported with its first question unreadable, so every value here goes into the
template's shared-strings table and every other part of the package is copied byte for byte.
"""

import re
import zipfile
from dataclasses import dataclass
from xml.sax.saxutils import escape

from ooxml_read import SHARED_STRINGS, data_row_format, header_columns, sheet_path, shared_strings

HEADER_ROWS = 1


@dataclass
class RowFormat:
    columns: list
    attrs: str
    styles: dict
    index: dict

    def cell(self, column, number, text):
        style = " " + self.styles[column] if column in self.styles else ""
        return '<c r="%s%d"%s t="s"><v>%d</v></c>' % (column, number, style, self.index[text])

    def row(self, number, values):
        attrs = re.sub(r'\s*\br="\d+"', "", self.attrs)
        cells = "".join(self.cell(column, number, text) for column, text in zip(self.columns, values) if text)
        return '<row r="%d"%s>%s</row>' % (number, attrs, cells)


def string_indexes(rows, existing):
    index = {text: number for number, text in enumerate(existing)}
    added = []
    for row in rows:
        for text in row:
            if text and text not in index:
                index[text] = len(existing) + len(added)
                added.append(text)
    return index, added


def replace_sheet_data(sheet_xml, data_rows, last_column):
    header = re.search(r'<row r="1"[ >].*?</row>', sheet_xml, re.DOTALL).group(0)
    start = sheet_xml.index("<sheetData>") + len("<sheetData>")
    end = sheet_xml.index("</sheetData>")
    filled = sheet_xml[:start] + header + "".join(data_rows) + sheet_xml[end:]
    last_row = HEADER_ROWS + len(data_rows)
    return re.sub(r'<dimension ref="[^"]*"/>', '<dimension ref="A1:%s%d"/>' % (last_column, last_row), filled)


def append_shared_strings(sst_xml, added, references):
    items = "".join('<si><t xml:space="preserve">%s</t></si>' % escape(text) for text in added)
    count = re.search(r'\bcount="(\d+)"', sst_xml)
    unique = int(re.search(r'uniqueCount="(\d+)"', sst_xml).group(1)) + len(added)
    if count:
        sst_xml = re.sub(r'\bcount="\d+"', 'count="%d"' % (int(count.group(1)) + references), sst_xml, count=1)
    sst_xml = re.sub(r'uniqueCount="\d+"', 'uniqueCount="%d"' % unique, sst_xml, count=1)
    return sst_xml.replace("</sst>", items + "</sst>")


def read_header(template, sheet_name=None):
    with zipfile.ZipFile(template) as package:
        _, path = sheet_path(package, sheet_name)
        return [text for _, text in header_columns(package.read(path).decode("utf-8"), shared_strings(package))]


def fill_template(template, rows, output, sheet_name=None):
    with zipfile.ZipFile(template) as package, zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as result:
        name, path = sheet_path(package, sheet_name)
        existing = shared_strings(package)
        sheet_xml = package.read(path).decode("utf-8")
        columns = [column for column, _ in header_columns(sheet_xml, existing)]
        attrs, styles = data_row_format(sheet_xml)
        index, added = string_indexes(rows, existing)
        row_format = RowFormat(columns, attrs, styles, index)
        data_rows = [row_format.row(number, values) for number, values in enumerate(rows, start=HEADER_ROWS + 1)]
        references = sum(1 for row in rows for text in row if text)
        for info in package.infolist():
            data = package.read(info.filename)
            if info.filename == path:
                data = replace_sheet_data(sheet_xml, data_rows, columns[-1]).encode("utf-8")
            elif info.filename == SHARED_STRINGS:
                data = append_shared_strings(data.decode("utf-8"), added, references).encode("utf-8")
            result.writestr(info, data)
    return name
