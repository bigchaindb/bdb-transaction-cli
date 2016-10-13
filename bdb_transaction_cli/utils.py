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
