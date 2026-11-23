"""Build Edlink quiz import files (.xlsx) from quiz specs in JSON, one file per spec.

    python make_quiz.py --template import-quiz-questions.xlsx quiz4.json quiz5.json
    python make_quiz.py --template import-quiz-questions.xlsx --check quiz4.json
"""

import argparse
import json
import sys
from pathlib import Path

from ooxml_read import TemplateError
from xlsx_template import fill_template

WRONG_ANSWERS = 4
MAX_FIELD_LENGTH = 3000


def check_question(number, item):
    choices = [item["correct"], *item["wrong"]]
    texts = [item["question"], *choices]
    if len(item["wrong"]) != WRONG_ANSWERS:
        raise TemplateError("question %d: needs %d wrong answers, has %d" % (number, WRONG_ANSWERS, len(item["wrong"])))
    if any(not str(text).strip() for text in texts):
        raise TemplateError("question %d: empty text" % number)
    if len(set(choices)) != len(choices):
        raise TemplateError("question %d: two choices are identical" % number)
    if any(len(str(text)) > MAX_FIELD_LENGTH for text in texts):
        raise TemplateError("question %d: a field is longer than %d characters" % (number, MAX_FIELD_LENGTH))
    return [str(text) for text in texts]


def read_spec(path):
    spec = json.loads(path.read_text(encoding="utf-8"))
    try:
        return [check_question(number, item) for number, item in enumerate(spec["questions"], start=1)]
    except KeyError as key:
        raise TemplateError("missing field %s" % key) from key


def build(path, template, check_only):
    rows = read_spec(path)
    if not check_only:
        fill_template(template, rows, path.with_suffix(".xlsx"))
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("specs", type=Path, nargs="+")
    parser.add_argument("--template", type=Path, required=True, help="import-quiz-questions.xlsx from Edlink")
    parser.add_argument("--check", action="store_true", help="validate the specs without writing files")
    args = parser.parse_args()
    failed = 0
    for path in args.specs:
        try:
            print("%s: %d question(s)" % (path.name, build(path, args.template, args.check)))
        except TemplateError as error:
            print("%s: %s" % (path.name, error), file=sys.stderr)
            failed += 1
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
