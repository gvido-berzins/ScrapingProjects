from pysqlite3._sqlite3 import *
import datetime
from _typeshed import Incomplete

paramstyle: str
threadsafety: int
apilevel: str
Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime

def DateFromTicks(ticks): ...
def TimeFromTicks(ticks): ...
def TimestampFromTicks(ticks): ...

version_info: Incomplete
sqlite_version_info: Incomplete
Binary = memoryview

def register_adapters_and_converters(): ...
