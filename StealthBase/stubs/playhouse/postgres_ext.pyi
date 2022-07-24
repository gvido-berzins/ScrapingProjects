from peewee import *
from _typeshed import Incomplete
from collections.abc import Generator
from peewee import ColumnBase, Node, __exception_wrapper__ as __exception_wrapper__

logger: Incomplete
HCONTAINS_DICT: str
HCONTAINS_KEYS: str
HCONTAINS_KEY: str
HCONTAINS_ANY_KEY: str
HKEY: str
HUPDATE: str
ACONTAINS: str
ACONTAINED_BY: str
ACONTAINS_ANY: str
TS_MATCH: str
JSONB_CONTAINS: str
JSONB_CONTAINED_BY: str
JSONB_CONTAINS_KEY: str
JSONB_CONTAINS_ANY_KEY: str
JSONB_CONTAINS_ALL_KEYS: str
JSONB_EXISTS: str
JSONB_REMOVE: str

class _LookupNode(ColumnBase):
    node: Incomplete
    parts: Incomplete
    def __init__(self, node, parts) -> None: ...
    def clone(self): ...
    def __hash__(self): ...

class _JsonLookupBase(_LookupNode):
    def __init__(self, node, parts, as_json: bool = ...) -> None: ...
    def clone(self): ...
    def as_json(self, as_json: bool = ...) -> None: ...
    def concat(self, rhs): ...
    def contains(self, other): ...
    def contains_any(self, *keys): ...
    def contains_all(self, *keys): ...
    def has_key(self, key): ...

class JsonLookup(_JsonLookupBase):
    def __getitem__(self, value): ...
    def __sql__(self, ctx): ...

class JsonPath(_JsonLookupBase):
    def __sql__(self, ctx): ...

class ObjectSlice(_LookupNode):
    @classmethod
    def create(cls, node, value): ...
    def __sql__(self, ctx): ...
    def __getitem__(self, value): ...

class IndexedFieldMixin:
    default_index_type: str
    def __init__(self, *args, **kwargs) -> None: ...

class ArrayField(IndexedFieldMixin, Field):
    passthrough: bool
    dimensions: Incomplete
    convert_values: Incomplete
    field_type: Incomplete
    def __init__(self, field_class=..., field_kwargs: Incomplete | None = ..., dimensions: int = ..., convert_values: bool = ..., *args, **kwargs) -> None: ...
    def bind(self, model, name, set_attribute: bool = ...): ...
    def ddl_datatype(self, ctx): ...
    def db_value(self, value): ...
    def python_value(self, value): ...
    def __getitem__(self, value): ...
    __eq__: Incomplete
    __ne__: Incomplete
    __gt__: Incomplete
    __ge__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete
    __hash__: Incomplete
    def contains(self, *items): ...
    def contains_any(self, *items): ...
    def contained_by(self, *items): ...

class ArrayValue(Node):
    field: Incomplete
    value: Incomplete
    def __init__(self, field, value) -> None: ...
    def __sql__(self, ctx): ...

class DateTimeTZField(DateTimeField):
    field_type: str

class HStoreField(IndexedFieldMixin, Field):
    field_type: str
    __hash__: Incomplete
    def __getitem__(self, key): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def slice(self, *args): ...
    def exists(self, key): ...
    def defined(self, key): ...
    def update(self, **data): ...
    def delete(self, *keys): ...
    def contains(self, value): ...
    def contains_any(self, *keys): ...

class JSONField(Field):
    field_type: str
    dumps: Incomplete
    def __init__(self, dumps: Incomplete | None = ..., *args, **kwargs) -> None: ...
    def db_value(self, value): ...
    def __getitem__(self, value): ...
    def path(self, *keys): ...
    def concat(self, value): ...

def cast_jsonb(node): ...

class BinaryJSONField(IndexedFieldMixin, JSONField):
    field_type: str
    __hash__: Incomplete
    def contains(self, other): ...
    def contained_by(self, other): ...
    def contains_any(self, *items): ...
    def contains_all(self, *items): ...
    def has_key(self, key): ...
    def remove(self, *items): ...

class TSVectorField(IndexedFieldMixin, TextField):
    field_type: str
    __hash__: Incomplete
    def match(self, query, language: Incomplete | None = ..., plain: bool = ...): ...

def Match(field, query, language: Incomplete | None = ...): ...

class IntervalField(Field):
    field_type: str

class FetchManyCursor:
    cursor: Incomplete
    array_size: Incomplete
    exhausted: bool
    iterable: Incomplete
    def __init__(self, cursor, array_size: Incomplete | None = ...) -> None: ...
    @property
    def description(self): ...
    def close(self) -> None: ...
    def row_gen(self) -> Generator[Incomplete, None, None]: ...
    def fetchone(self): ...

class ServerSideQuery(Node):
    query: Incomplete
    array_size: Incomplete
    def __init__(self, query, array_size: Incomplete | None = ...) -> None: ...
    def __sql__(self, ctx): ...
    def __iter__(self): ...

def ServerSide(query, database: Incomplete | None = ..., array_size: Incomplete | None = ...) -> Generator[Incomplete, None, None]: ...

class _empty_object:
    def __nonzero__(self): ...
    __bool__: Incomplete

__named_cursor__: Incomplete

class PostgresqlExtDatabase(PostgresqlDatabase):
    def __init__(self, *args, **kwargs) -> None: ...
    def cursor(self, commit: Incomplete | None = ...): ...
    def execute(self, query, commit=..., named_cursor: bool = ..., array_size: Incomplete | None = ..., **context_options): ...
