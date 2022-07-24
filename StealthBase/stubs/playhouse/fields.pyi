from _typeshed import Incomplete
from peewee import BlobField

class CompressedField(BlobField):
    ZLIB: str
    BZ2: str
    algorithm_to_import: Incomplete
    compression_level: Incomplete
    algorithm: Incomplete
    compress: Incomplete
    decompress: Incomplete
    def __init__(self, compression_level: int = ..., algorithm=..., *args, **kwargs) -> None: ...
    def python_value(self, value): ...
    def db_value(self, value): ...

class PickleField(BlobField):
    def python_value(self, value): ...
    def db_value(self, value): ...
