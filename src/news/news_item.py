import requests
import os


class NewsItem:
    title: str
    url: str
    image: str
    text: str
    opinion: str

    def _get_prefered_news_category(self):
        raise NotImplementedError(
            "This method should be implemented by the subclass")

    def get_news_info(self):
        raise NotImplementedError(
            "This method should be implemented by the subclass")

    def save_picture(self):
        response = requests.get(self.image)
        path = os.path.join(os.getcwd(), "data/images")
        with open(f"{path}/{self.title}.jpg", "wb") as file:
            file.write(response.content)
