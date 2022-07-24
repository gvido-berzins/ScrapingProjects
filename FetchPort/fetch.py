import click
import pandas as pd
from requests_html import HTMLSession

BASE_URL = "https://www.speedguide.net"
PORT_URL = f"{BASE_URL}/port.php"


def fetch(port: int):
    url = f"{BASE_URL}/port.php?port={port}"
    print(f"URL: {url}")
    s = HTMLSession()
    r = s.get(url)
    if not r.ok:
        raise RuntimeError(f"Failed to query given port: {port}")
    return r.html


def extract(r) -> pd.DataFrame:
    t = r.find("table.port", first=True).html
    df = pd.read_html(t)[0]
    df = df[["Port(s)", "Protocol", "Service", "Details"]]
    df.Service = df.Service.fillna("unknown")
    df = clean_df(df)
    return df


def extract_external(r) -> pd.DataFrame:
    selector = "//p/b[contains(text(), 'External Resources')]/following-sibling::a"
    d = tuple((e.attrs["href"], e.text) for e in r.xpath(selector))
    df = pd.DataFrame(d, columns=["url", "title"])
    df = clean_df(df)
    return df


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.select_dtypes(["object"]).apply(lambda x: x.str.strip())
    return df


def show(*dfs: pd.DataFrame) -> None:
    print("show".center(70, "-"))
    for df in dfs:
        for row in df.iterrows():
            print(row)
            print()
    print()


def to_csv(filename, df: pd.DataFrame) -> None:
    df.to_csv(filename, index=False)
    print(f"Saved to {filename!r}")


@click.argument("port", type=int)
@click.command()
def cli(port):
    r = fetch(port)
    df_info = extract(r)
    df_links = extract_external(r)
    # show(df_info, df_links)
    to_csv(f"p{port}_info.csv", df_info)


if __name__ == "__main__":
    raise SystemExit(cli())
