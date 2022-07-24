from typing import Any

import pysqlite3.dbapi2
PARSE_COLNAMES: int
PARSE_DECLTYPES: int
SQLITE_ABORT: int
SQLITE_ALTER_TABLE: int
SQLITE_ANALYZE: int
SQLITE_ATTACH: int
SQLITE_AUTH: int
SQLITE_BUSY: int
SQLITE_CANTOPEN: int
SQLITE_CONSTRAINT: int
SQLITE_CORRUPT: int
SQLITE_CREATE_INDEX: int
SQLITE_CREATE_TABLE: int
SQLITE_CREATE_TEMP_INDEX: int
SQLITE_CREATE_TEMP_TABLE: int
SQLITE_CREATE_TEMP_TRIGGER: int
SQLITE_CREATE_TEMP_VIEW: int
SQLITE_CREATE_TRIGGER: int
SQLITE_CREATE_VIEW: int
SQLITE_CREATE_VTABLE: int
SQLITE_DELETE: int
SQLITE_DENY: int
SQLITE_DETACH: int
SQLITE_DONE: int
SQLITE_DROP_INDEX: int
SQLITE_DROP_TABLE: int
SQLITE_DROP_TEMP_INDEX: int
SQLITE_DROP_TEMP_TABLE: int
SQLITE_DROP_TEMP_TRIGGER: int
SQLITE_DROP_TEMP_VIEW: int
SQLITE_DROP_TRIGGER: int
SQLITE_DROP_VIEW: int
SQLITE_DROP_VTABLE: int
SQLITE_EMPTY: int
SQLITE_ERROR: int
SQLITE_FORMAT: int
SQLITE_FULL: int
SQLITE_FUNCTION: int
SQLITE_IGNORE: int
SQLITE_INSERT: int
SQLITE_INTERNAL: int
SQLITE_INTERRUPT: int
SQLITE_IOERR: int
SQLITE_LOCKED: int
SQLITE_MISMATCH: int
SQLITE_MISUSE: int
SQLITE_NOLFS: int
SQLITE_NOMEM: int
SQLITE_NOTADB: int
SQLITE_NOTFOUND: int
SQLITE_OK: int
SQLITE_OPEN_CREATE: int
SQLITE_OPEN_FULLMUTEX: int
SQLITE_OPEN_MEMORY: int
SQLITE_OPEN_NOMUTEX: int
SQLITE_OPEN_PRIVATECACHE: int
SQLITE_OPEN_READONLY: int
SQLITE_OPEN_READWRITE: int
SQLITE_OPEN_SHAREDCACHE: int
SQLITE_OPEN_URI: int
SQLITE_PERM: int
SQLITE_PRAGMA: int
SQLITE_PROTOCOL: int
SQLITE_RANGE: int
SQLITE_READ: int
SQLITE_READONLY: int
SQLITE_RECURSIVE: int
SQLITE_REINDEX: int
SQLITE_ROW: int
SQLITE_SAVEPOINT: int
SQLITE_SCHEMA: int
SQLITE_SELECT: int
SQLITE_TOOBIG: int
SQLITE_TRANSACTION: int
SQLITE_UPDATE: int
adapters: dict
converters: dict
sqlite_version: str
version: str

class Cache:
    def __init__(self, *args, **kwargs) -> None: ...
    def display(self, *args, **kwargs) -> Any: ...
    def get(self, *args, **kwargs) -> Any: ...

class Connection:
    DataError: Any
    DatabaseError: Any
    Error: Any
    IntegrityError: Any
    InterfaceError: Any
    InternalError: Any
    NotSupportedError: Any
    OperationalError: Any
    ProgrammingError: Any
    Warning: Any
    in_transaction: Any
    isolation_level: Any
    row_factory: Any
    text_factory: Any
    total_changes: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def backup(self, *args, **kwargs) -> Any: ...
    def close(self, *args, **kwargs) -> Any: ...
    def commit(self, *args, **kwargs) -> Any: ...
    def create_aggregate(self, *args, **kwargs) -> Any: ...
    def create_collation(self, *args, **kwargs) -> Any: ...
    def create_function(self, *args, **kwargs) -> Any: ...
    def create_window_function(self, *args, **kwargs) -> Any: ...
    def cursor(self, *args, **kwargs) -> Any: ...
    def enable_load_extension(self, *args, **kwargs) -> Any: ...
    def execute(self, *args, **kwargs) -> Any: ...
    def executemany(self, *args, **kwargs) -> Any: ...
    def executescript(self, *args, **kwargs) -> Any: ...
    def interrupt(self, *args, **kwargs) -> Any: ...
    def load_extension(self, *args, **kwargs) -> Any: ...
    def open_blob(self, *args, **kwargs) -> Any: ...
    def rollback(self, *args, **kwargs) -> Any: ...
    def set_authorizer(self, *args, **kwargs) -> Any: ...
    def set_progress_handler(self, *args, **kwargs) -> Any: ...
    def set_trace_callback(self, *args, **kwargs) -> Any: ...
    def __call__(self, *args, **kwargs) -> Any: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, type, value, traceback) -> Any: ...

class Cursor:
    arraysize: Any
    connection: Any
    description: Any
    lastrowid: Any
    row_factory: Any
    rowcount: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    def execute(self, *args, **kwargs) -> Any: ...
    def executemany(self, *args, **kwargs) -> Any: ...
    def executescript(self, *args, **kwargs) -> Any: ...
    def fetchall(self, *args, **kwargs) -> Any: ...
    def fetchmany(self, *args, **kwargs) -> Any: ...
    def fetchone(self, *args, **kwargs) -> Any: ...
    def setinputsizes(self, *args, **kwargs) -> Any: ...
    def setoutputsize(self, *args, **kwargs) -> Any: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...

class DataError(pysqlite3.dbapi2.DatabaseError): ...

class DatabaseError(pysqlite3.dbapi2.Error): ...

class Error(Exception): ...

class IntegrityError(pysqlite3.dbapi2.DatabaseError): ...

class InterfaceError(pysqlite3.dbapi2.Error): ...

class InternalError(pysqlite3.dbapi2.DatabaseError): ...

class NotSupportedError(pysqlite3.dbapi2.DatabaseError): ...

class OperationalError(pysqlite3.dbapi2.DatabaseError): ...

class OptimizedUnicode:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def capitalize(self, *args, **kwargs) -> Any: ...
    def casefold(self, *args, **kwargs) -> Any: ...
    def center(self, *args, **kwargs) -> Any: ...
    def count(self, *args, **kwargs) -> Any: ...
    def encode(self, *args, **kwargs) -> Any: ...
    def endswith(self, *args, **kwargs) -> Any: ...
    def expandtabs(self, *args, **kwargs) -> Any: ...
    def find(self, *args, **kwargs) -> Any: ...
    def format(self, *args, **kwargs) -> str: ...
    def format_map(self, mapping) -> str: ...
    def index(self, *args, **kwargs) -> Any: ...
    def isalnum(self, *args, **kwargs) -> Any: ...
    def isalpha(self, *args, **kwargs) -> Any: ...
    def isascii(self, *args, **kwargs) -> Any: ...
    def isdecimal(self, *args, **kwargs) -> Any: ...
    def isdigit(self, *args, **kwargs) -> Any: ...
    def isidentifier(self, *args, **kwargs) -> Any: ...
    def islower(self, *args, **kwargs) -> Any: ...
    def isnumeric(self, *args, **kwargs) -> Any: ...
    def isprintable(self, *args, **kwargs) -> Any: ...
    def isspace(self, *args, **kwargs) -> Any: ...
    def istitle(self, *args, **kwargs) -> Any: ...
    def isupper(self, *args, **kwargs) -> Any: ...
    def join(self, *args, **kwargs) -> Any: ...
    def ljust(self, *args, **kwargs) -> Any: ...
    def lower(self, *args, **kwargs) -> Any: ...
    def lstrip(self, *args, **kwargs) -> Any: ...
    def maketrans(self, *args, **kwargs) -> Any: ...
    def partition(self, *args, **kwargs) -> Any: ...
    def removeprefix(self, *args, **kwargs) -> Any: ...
    def removesuffix(self, *args, **kwargs) -> Any: ...
    def replace(self, *args, **kwargs) -> Any: ...
    def rfind(self, *args, **kwargs) -> Any: ...
    def rindex(self, *args, **kwargs) -> Any: ...
    def rjust(self, *args, **kwargs) -> Any: ...
    def rpartition(self, *args, **kwargs) -> Any: ...
    def rsplit(self, *args, **kwargs) -> Any: ...
    def rstrip(self, *args, **kwargs) -> Any: ...
    def split(self, *args, **kwargs) -> Any: ...
    def splitlines(self, *args, **kwargs) -> Any: ...
    def startswith(self, *args, **kwargs) -> Any: ...
    def strip(self, *args, **kwargs) -> Any: ...
    def swapcase(self, *args, **kwargs) -> Any: ...
    def title(self, *args, **kwargs) -> Any: ...
    def translate(self, *args, **kwargs) -> Any: ...
    def upper(self, *args, **kwargs) -> Any: ...
    def zfill(self, *args, **kwargs) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __format__(self, *args, **kwargs) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __getnewargs__(self, *args, **kwargs) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __iter__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __len__(self) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __sizeof__(self) -> Any: ...

class PrepareProtocol:
    def __init__(self, *args, **kwargs) -> None: ...

class ProgrammingError(pysqlite3.dbapi2.DatabaseError): ...

class Row:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def keys(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __iter__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __len__(self) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...

class Statement:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...

class Warning(Exception): ...

def adapt(*args, **kwargs) -> Any: ...
def complete_statement(sql) -> Any: ...
def connect(*args, **kwargs) -> Any: ...
def enable_callback_tracebacks(flag) -> Any: ...
def enable_shared_cache(do_enable) -> Any: ...
def register_adapter(type, callable) -> Any: ...
def register_converter(typename, callable) -> Any: ...
