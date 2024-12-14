from .news_item import NewsItem
import bbc
from web_scraping.scraping import get_soup
import requests
import os


class InternationalNewsItem(NewsItem):

    def __init__(self):
        self.title = ""
        self.url = ""
        self.image = ""
        self.text = ""
        self.news = bbc.news.get_news(bbc.Languages.Spanish)

    def _get_prefered_news_category(self) -> str:
        print("Escoja su categoría preferida: ")
        categories = self.news.news_categories()
        filtered_categories = [category for category in categories if category not in [
            "Video y audio", "En fotos", "En redes sociales"]]
        for index, category in enumerate(filtered_categories):
            print(f"{index + 1} - {category}")
        while True:
            try:
                category_index = int(
                    input("Ingrese el número de la categoría: ")) - 1
                print(f"La categoría seleccionada es: {
                      filtered_categories[category_index]}")
                break
            except Exception as e:
                print("Error al seleccionar la categoría")

        return filtered_categories[category_index]

    def _get_prefered_news_item(self) -> dict:
        category = self._get_prefered_news_category()
        print("Escoja su noticia preferida: ")
        news = self.news.news_category(category)
        only_bbc_news = [
            item for item in news if item["news_link"].startswith("https://www.bbc.com")]
        for index, item in enumerate(only_bbc_news):
            print(f"{index + 1} - {item["title"]}")
        while True:
            try:
                item_index = int(
                    input("Ingrese el número de la noticia: ")) - 1
                print(f"La noticia seleccionada es: {
                      only_bbc_news[item_index]["title"]}")
                break
            except Exception as e:
                print("Error al seleccionar la noticia")
        return only_bbc_news[item_index]

    def _get_news_text(self):
        soup = get_soup(url=self.url)
        parragraphs = soup.find_all("p")
        parragraphs = parragraphs[:-5]
        for parragraph in parragraphs:
            self.text += parragraph.text

    def save_picture(self):
        response = requests.get(self.image)
        path = os.path.join(os.getcwd(), "data/images")
        with open(f"{path}/{self.title}.jpg", "wb") as file:
            file.write(response.content)

    def get_news_info(self):
        newsItem = self._get_prefered_news_item()

        self.title = newsItem["title"]
        self.url = newsItem["news_link"]
        image = newsItem["image_link"].replace(
            "/240", "/1024")
        self.image = image.replace(".webp", "")
        self._get_news_text()
        self.save_picture()
