from peewee import *
from _typeshed import Incomplete
from peewee import SCOPE_VALUES as SCOPE_VALUES
from playhouse import postgres_ext as postgres_ext
from playhouse.cockroachdb import CockroachDatabase as CockroachDatabase
from typing import NamedTuple

OrderedDict = dict
RESERVED_WORDS: Incomplete

class UnknownField: ...

class Column:
    primary_key_types: Incomplete
    name: Incomplete
    field_class: Incomplete
    raw_column_type: Incomplete
    nullable: Incomplete
    primary_key: Incomplete
    column_name: Incomplete
    index: Incomplete
    unique: Incomplete
    default: Incomplete
    extra_parameters: Incomplete
    rel_model: Incomplete
    related_name: Incomplete
    to_field: Incomplete
    def __init__(self, name, field_class, raw_column_type, nullable, primary_key: bool = ..., column_name: Incomplete | None = ..., index: bool = ..., unique: bool = ..., default: Incomplete | None = ..., extra_parameters: Incomplete | None = ...) -> None: ...
    def get_field_parameters(self): ...
    def is_primary_key(self): ...
    def is_foreign_key(self): ...
    def is_self_referential_fk(self): ...
    foreign_key: Incomplete
    def set_foreign_key(self, foreign_key, model_names, dest: Incomplete | None = ..., related_name: Incomplete | None = ...) -> None: ...
    def get_field(self): ...

class Metadata:
    column_map: Incomplete
    extension_import: str
    database: Incomplete
    requires_extension: bool
    def __init__(self, database) -> None: ...
    def execute(self, sql, *params): ...
    def get_columns(self, table, schema: Incomplete | None = ...): ...
    def get_column_types(self, table, schema: Incomplete | None = ...) -> None: ...
    def get_foreign_keys(self, table, schema: Incomplete | None = ...): ...
    def get_primary_keys(self, table, schema: Incomplete | None = ...): ...
    def get_indexes(self, table, schema: Incomplete | None = ...): ...

class PostgresqlMetadata(Metadata):
    column_map: Incomplete
    array_types: Incomplete
    extension_import: str
    def __init__(self, database) -> None: ...
    requires_extension: bool
    def get_column_types(self, table, schema): ...
    def get_columns(self, table, schema: Incomplete | None = ...): ...
    def get_foreign_keys(self, table, schema: Incomplete | None = ...): ...
    def get_primary_keys(self, table, schema: Incomplete | None = ...): ...
    def get_indexes(self, table, schema: Incomplete | None = ...): ...

class CockroachDBMetadata(PostgresqlMetadata):
    column_map: Incomplete
    array_types: Incomplete
    extension_import: str
    requires_extension: bool
    def __init__(self, database) -> None: ...

class MySQLMetadata(Metadata):
    column_map: Incomplete
    def __init__(self, database, **kwargs) -> None: ...
    def get_column_types(self, table, schema: Incomplete | None = ...): ...

class SqliteMetadata(Metadata):
    column_map: Incomplete
    begin: str
    end: str
    re_foreign_key: Incomplete
    re_varchar: str
    def get_column_types(self, table, schema: Incomplete | None = ...): ...

class _DatabaseMetadata(NamedTuple):
    columns: Incomplete
    primary_keys: Incomplete
    foreign_keys: Incomplete
    model_names: Incomplete
    indexes: Incomplete

class DatabaseMetadata(_DatabaseMetadata):
    def multi_column_indexes(self, table): ...
    def column_indexes(self, table): ...

class Introspector:
    pk_classes: Incomplete
    metadata: Incomplete
    schema: Incomplete
    def __init__(self, metadata, schema: Incomplete | None = ...) -> None: ...
    @classmethod
    def from_database(cls, database, schema: Incomplete | None = ...): ...
    def get_database_class(self): ...
    def get_database_name(self): ...
    def get_database_kwargs(self): ...
    def get_additional_imports(self): ...
    def make_model_name(self, table, snake_case: bool = ...): ...
    def make_column_name(self, column, is_foreign_key: bool = ..., snake_case: bool = ...): ...
    def introspect(self, table_names: Incomplete | None = ..., literal_column_names: bool = ..., include_views: bool = ..., snake_case: bool = ...): ...
    def generate_models(self, skip_invalid: bool = ..., table_names: Incomplete | None = ..., literal_column_names: bool = ..., bare_fields: bool = ..., include_views: bool = ...): ...

def introspect(database, schema: Incomplete | None = ...): ...
def generate_models(database, schema: Incomplete | None = ..., **options): ...
def print_model(model, indexes: bool = ..., inline_indexes: bool = ...) -> None: ...
def get_table_sql(model): ...
def print_table_sql(model) -> None: ...
