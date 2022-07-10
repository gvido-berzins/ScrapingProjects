from typing import List

import pandas as pd
from pydantic import BaseModel, parse_obj_as
import requests

OS_DICT = {1: "Linux", 2: "Windows", 3: "Other", 4: "Unknown"}
LEVEL_DICT = {1: "Easy", 2: "Intermediate", 3: "Hard"}


class Machine(BaseModel):
    primary_os: str
    name: str
    difficulty: str
    display_description: str

    def __init__(self, **kwargs):
        os = kwargs.get("primary_os")
        kwargs["primary_os"] = OS_DICT.get(os, str(os))
        kwargs["difficulty"] = LEVEL_DICT.get(kwargs.get("difficulty"))
        super().__init__(**kwargs)

    @property
    def os(self) -> str:
        return OS_DICT.get(self.primary_os, "Unrecognized")


def fetch_json(url):
    res = requests.get(url)
    return res.json()


def extract(data: dict) -> List[Machine]:
    return parse_obj_as(List[Machine], find_all(data))


def find_all(data) -> list[dict]:
    for lab_group in data["children"]:
        if lab_group.get("name") == "All":
            return lab_group["children"]
    else:
        return []


def save(machines: List[Machine], filename: str = "machines.xlsx") -> None:
    # df = pd.DataFrame.from_records(machines)
    data = [m.dict() for m in machines]
    df = pd.json_normalize(data)
    df.to_excel(filename, index=False)
    print(f"Saved to {filename!r}")


def main():
    url = "https://portal.offensive-security.com/api/learning-units/2/full"
    json_data = fetch_json(url)
    machines = extract(json_data)
    save(machines)


if __name__ == "__main__":
    raise SystemExit(main())
