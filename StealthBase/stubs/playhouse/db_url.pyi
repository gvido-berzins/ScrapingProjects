from peewee import *
from _typeshed import Incomplete
from playhouse.apsw_ext import APSWDatabase as APSWDatabase
from playhouse.cockroachdb import CockroachDatabase as CockroachDatabase, PooledCockroachDatabase as PooledCockroachDatabase
from playhouse.pool import PooledMySQLDatabase as PooledMySQLDatabase, PooledPostgresqlDatabase as PooledPostgresqlDatabase, PooledPostgresqlExtDatabase as PooledPostgresqlExtDatabase, PooledSqliteDatabase as PooledSqliteDatabase, PooledSqliteExtDatabase as PooledSqliteExtDatabase
from playhouse.postgres_ext import PostgresqlExtDatabase as PostgresqlExtDatabase
from playhouse.sqlite_ext import SqliteExtDatabase as SqliteExtDatabase

schemes: Incomplete

def register_database(db_class, *names) -> None: ...
def parseresult_to_dict(parsed, unquote_password: bool = ...): ...
def parse(url, unquote_password: bool = ...): ...
def connect(url, unquote_password: bool = ..., **connect_params): ...
