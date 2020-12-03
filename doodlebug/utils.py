import json
import datetime
from typing import Any

from starlette.responses import Response

from doodlebug.config import settings


class DateTimeEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()

        return super(DateTimeEncoder, self).default(obj)


class JSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:

        args = {}
        if settings.development:
            args["indent"] = 4

        return json.dumps(
            content,
            cls=DateTimeEncoder,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
            **args,
        ).encode("utf-8")


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


class BaseConfig:
    alias_generator = to_camel_case
    allow_population_by_field_name = True
