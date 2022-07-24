from peewee import *
from _typeshed import Incomplete
from playhouse.sqlite_ext import JSONField as JSONField

class BaseChangeLog(Model):
    timestamp: Incomplete
    action: Incomplete
    table: Incomplete
    primary_key: Incomplete
    changes: Incomplete

class ChangeLog:
    base_model: Incomplete
    template: str
    drop_template: str
    db: Incomplete
    table_name: Incomplete
    def __init__(self, db, table_name: str = ...) -> None: ...
    def trigger_sql(self, model, action, skip_fields: Incomplete | None = ...): ...
    def drop_trigger_sql(self, model, action): ...
    @property
    def model(self): ...
    def install(self, model, skip_fields: Incomplete | None = ..., drop: bool = ..., insert: bool = ..., update: bool = ..., delete: bool = ..., create_table: bool = ...) -> None: ...
