from typing import List, Dict
from bs4 import BeautifulSoup
from .interfaces.html_collector import HtmlCollectorInterface


class HtmlCollector(HtmlCollectorInterface):

    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, "html.parser")

        artist_name_list = soup.find(class_="BodyText")
        artist_name_list_items = artist_name_list.find_all("a")

        links = "https://web.archive.org"
        essential_information = [
            {"name": artist_name.contents[0],
             "link": links + artist_name.get("href")}
            for artist_name in artist_name_list_items]
        return essential_information
