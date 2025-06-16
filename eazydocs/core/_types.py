from typing import NamedTuple, TypedDict


class ParamsDict(TypedDict):
    arg_type: str
    description: str
    default_value: str


class ArgsTuple(NamedTuple):
    param: str
    arg_type: str
    description: str
