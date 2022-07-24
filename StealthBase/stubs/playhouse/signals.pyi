from _typeshed import Incomplete
from peewee import Model as _Model

class Signal:
    def __init__(self) -> None: ...
    def connect(self, receiver, name: Incomplete | None = ..., sender: Incomplete | None = ...) -> None: ...
    def disconnect(self, receiver: Incomplete | None = ..., name: Incomplete | None = ..., sender: Incomplete | None = ...) -> None: ...
    def __call__(self, name: Incomplete | None = ..., sender: Incomplete | None = ...): ...
    def send(self, instance, *args, **kwargs): ...

pre_save: Incomplete
post_save: Incomplete
pre_delete: Incomplete
post_delete: Incomplete
pre_init: Incomplete

class Model(_Model):
    def __init__(self, *args, **kwargs) -> None: ...
    def save(self, *args, **kwargs): ...
    def delete_instance(self, *args, **kwargs): ...
