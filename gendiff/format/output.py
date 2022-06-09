from .json import json_format
from .plain import plain
from .stylish import stylish

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def form_output(result, style):
    if style == STYLISH:
        return stylish(result)
    elif style == PLAIN:
        return plain(result)
    elif style == JSON:
        return json_format(result)
