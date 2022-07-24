from pathlib import Path

from environs import Env
from peewee import CharField, Model, MySQLDatabase, IntegerField
from playhouse.db_url import connect

from free_proxies.items import ProxyItem as Proxy
from test_urls import import_proxies


env = Env()
env.read_env()
db = connect(env("MYSQL_DATABASE_URL"))


class BaseModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = db


class Proxies(BaseModel):
    ip = CharField()
    port = IntegerField()
    protocol = CharField()


def create_tables(tables: list[Model], delete: bool = False) -> None:
    if delete:
        db.drop_tables(tables)
    db.create_tables(tables)


def main() -> int:
    create_tables([Proxies])
    path = Path("./good_proxies.json")
    proxies = import_proxies(path)
    Proxies.insert_many([x.dict() for x in proxies]).execute()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
