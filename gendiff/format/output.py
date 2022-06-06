from .json import json_format
from .plain import plain
from .stylish import stylish


def form_output(result, style):
    if style == 'stylish':
        return stylish(result)
    elif style == 'plain':
        return plain(result)
    elif style == 'json':
        return json_format(result)
