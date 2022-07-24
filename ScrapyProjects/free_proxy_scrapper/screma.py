import time
import ipaddress
from typing import Callable

import pydantic
import schema


SCHEMA = schema.Schema(
    dict(
        ip=schema.Use(ipaddress.ip_address),
        port=schema.Use(int)

    )
)


class Proxy(pydantic.BaseModel):
    ip: pydantic.IPvAnyAddress
    port: pydantic.conint(gt=0, lt=65356)



def bench_pydantic(data: dict):
    return Proxy.validate(data)


def bench_schema(data: dict) -> bool:
    return SCHEMA.validate(data)


def bench(data: dict, times: int, func: Callable[[dict], bool]) -> None:
    start = time.perf_counter()
    for _ in range(times):
        _ = func(data)

    print(f"Took: {time.perf_counter() - start}s")


data = dict(ip="0.0.0.0", port=9001)
times = 100000
bench(data, times, bench_pydantic)
bench(data, times, bench_schema)
