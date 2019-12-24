import json

from main import convert_to_html_string
from tests.examples import EXAMPLES


def main_test(index=0, all=False):
    if all:
        for json_str in EXAMPLES.keys():
            assert convert_to_html_string(json.loads(json_str)) == EXAMPLES[json_str]
    else:
        json_str = list(EXAMPLES.keys())[index]
        assert convert_to_html_string(json.loads(json_str)) == EXAMPLES[json_str]


if __name__ == "__main__":
    main_test(all=True)