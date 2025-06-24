import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    )
}

class Website:
    def __init__(self, url: str):
        self.url = url
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        self.html = resp.text
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.links = [a.get("href") for a in self.soup.find_all("a", href=True)]

    def get_contents(self) -> str:
        texts = list(self.soup.stripped_strings)
        return "\n\n".join(texts)
