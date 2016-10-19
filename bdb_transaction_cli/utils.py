import json

import click


class JsonParamType(click.ParamType):
    """ A Click parameter class that loads JSON """
    name = 'JSON'

    def convert(self, value, param, ctx):
        # No try-except in case `value is None`, as it is a valid value.
        # Still we want `json.loads` to visibly fail.
        if value is None:
            return value
        return json.loads(value)


def json_argument(*args, **kwargs):
    """ Decorator for a JSON command line argument """
    kwargs['type'] = JsonParamType()
    if 'help' in kwargs:
        del kwargs['help']
    return click.argument(*args, **kwargs)


def json_option(*args, **kwargs):
    """ Decorator for a JSON command line option """
    kwargs['type'] = JsonParamType()
    if 'help' in kwargs:
        del kwargs['help']
    return click.option(*args, **kwargs)


def listify(obj):
    """ Wrap something in a list, if it's not already a list """
    return obj if isinstance(obj, list) else [obj]
