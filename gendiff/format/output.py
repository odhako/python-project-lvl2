from .json import json_format
from .plain import plain
from .stylish import stylish

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def form_output(string_input, style):
    if style == STYLISH:
        return stylish(string_input)
    elif style == PLAIN:
        return plain(string_input)
    elif style == JSON:
        return json_format(string_input)
    else:
        raise Exception('Unknown style')
