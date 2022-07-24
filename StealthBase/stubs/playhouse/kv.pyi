from peewee import *
from _typeshed import Incomplete
from peewee import sqlite3 as sqlite3
from playhouse.fields import PickleField as PickleField
from playhouse.sqlite_ext import SqliteExtDatabase as SqliteExtDatabase

Sentinel: Incomplete

class KeyValue:
    upsert: Incomplete
    update: Incomplete
    model: Incomplete
    key: Incomplete
    value: Incomplete
    def __init__(self, key_field: Incomplete | None = ..., value_field: Incomplete | None = ..., ordered: bool = ..., database: Incomplete | None = ..., table_name: str = ...) -> None: ...
    def create_model(self): ...
    def query(self, *select): ...
    def convert_expression(self, expr): ...
    def __contains__(self, key): ...
    def __len__(self): ...
    def __getitem__(self, expr): ...
    def __setitem__(self, expr, value) -> None: ...
    def __delitem__(self, expr) -> None: ...
    def __iter__(self): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def get(self, key, default: Incomplete | None = ...): ...
    def setdefault(self, key, default: Incomplete | None = ...): ...
    def pop(self, key, default=...): ...
    def clear(self) -> None: ...