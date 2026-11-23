"""Fill any Edlink import template (RPS, Rincian RPS, quiz) from a JSON list of rows.

Rows are objects keyed by the template's header text, or plain lists in column order:

    python fill_template.py "Template Rincian RPS.xlsx" rincian.json -o Rincian_RPS_MK101.xlsx
    python fill_template.py "Template RPS.xlsx" --header
"""

import argparse
import json
import sys
from pathlib import Path

from ooxml_read import TemplateError
from xlsx_template import fill_template, read_header


def as_text(value):
    return "" if value is None else str(value).strip()


def to_row(item, header):
    if isinstance(item, list):
        if len(item) > len(header):
            raise TemplateError("a row has %d values but the template has %d columns" % (len(item), len(header)))
        return [as_text(value) for value in item]
    unknown = sorted(set(item) - set(header))
    if unknown:
        raise TemplateError("unknown column(s) %s; the template's columns are: %s" % (unknown, header))
    return [as_text(item.get(column)) for column in header]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("template", type=Path)
    parser.add_argument("data", type=Path, nargs="?")
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--sheet", help="sheet to fill (default: the first sheet)")
    parser.add_argument("--header", action="store_true", help="print the template's columns and stop")
    args = parser.parse_args()
    try:
        header = read_header(args.template, args.sheet)
        if args.header or args.data is None:
            print("\n".join(header))
            return
        rows = [to_row(item, header) for item in json.loads(args.data.read_text(encoding="utf-8"))]
        output = args.output or args.data.with_suffix(".xlsx")
        sheet = fill_template(args.template, rows, output, args.sheet)
    except TemplateError as error:
        sys.exit("error: %s" % error)
    print("%s: %d row(s) written to sheet %r" % (output, len(rows), sheet))


if __name__ == "__main__":
    main()
