from _typeshed import Incomplete
from itertools import chain as chain
from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase
from playhouse.postgres_ext import PostgresqlExtDatabase as PostgresqlExtDatabase
from playhouse.sqlite_ext import CSqliteExtDatabase as CSqliteExtDatabase, SqliteExtDatabase as SqliteExtDatabase
from typing import NamedTuple

logger: Incomplete

def make_int(val): ...

class MaxConnectionsExceeded(ValueError): ...

class PoolConnection(NamedTuple):
    timestamp: Incomplete
    connection: Incomplete
    checked_out: Incomplete

class PooledDatabase:
    conn_key: Incomplete
    def __init__(self, database, max_connections: int = ..., stale_timeout: Incomplete | None = ..., timeout: Incomplete | None = ..., **kwargs) -> None: ...
    def init(self, database, max_connections: Incomplete | None = ..., stale_timeout: Incomplete | None = ..., timeout: Incomplete | None = ..., **connect_kwargs) -> None: ...
    def connect(self, reuse_if_open: bool = ...): ...
    def manual_close(self): ...
    def close_idle(self) -> None: ...
    def close_stale(self, age: int = ...): ...
    def close_all(self) -> None: ...

class PooledMySQLDatabase(PooledDatabase, MySQLDatabase): ...
class _PooledPostgresqlDatabase(PooledDatabase): ...
class PooledPostgresqlDatabase(_PooledPostgresqlDatabase, PostgresqlDatabase): ...
class PooledPostgresqlExtDatabase(_PooledPostgresqlDatabase, PostgresqlExtDatabase): ...
class _PooledSqliteDatabase(PooledDatabase): ...
class PooledSqliteDatabase(_PooledSqliteDatabase, SqliteDatabase): ...
class PooledSqliteExtDatabase(_PooledSqliteDatabase, SqliteExtDatabase): ...
class PooledCSqliteExtDatabase(_PooledSqliteDatabase, CSqliteExtDatabase): ...