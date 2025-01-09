from web_scraping.scraping import get_soup
from .news_item import NewsItem
import json


class NationalNewsItem(NewsItem):

    def __init__(self, news_url, img_url):
        self.news_url = news_url
        self.img_url = img_url
        self.title = ""
        self.url = ""
        self.image = ""
        self.text = ""

    def _get_prefered_news_category(self, categories) -> int:
        print("Escoja su categoría preferida: ")
        for index, category in enumerate(categories):
            print(f"{index + 1} - {category}")
        while True:
            try:
                category_index = int(
                    input("Ingrese el número de la categoría: ")) - 1
                print(f"La categoría seleccionada es: {
                      categories[category_index]}")
                break
            except Exception as e:
                print("Error al seleccionar la categoría")
        return category_index

    def _get_news_text(self):
        soup = get_soup(url=self.url)
        parragraphs = soup.find_all("p")
        for parragraph in parragraphs:
            self.text += parragraph.text

    def get_news_info(self):
        soup = get_soup(url=self.news_url)
        script = soup.find(id="app-model")
        if script:
            data = json.loads(script.string)
            categories = []
            for news_item in data["globals"]:

                categories.append(news_item["post_categories"][0]["name"])

            category_index = self._get_prefered_news_category(categories)
            self.title = data["globals"][category_index]["post_title"]
            self.url = f"https://www.elcomercio.com/{
                data['globals'][category_index]['post_permalink']}"
            self.image = f"{self.img_url}{
                data['globals'][category_index]['post_images']['1024']}"
            self._get_news_text()
            self.save_picture()
