from news.national_news_item import NationalNewsItem
from news.international_news_item import InternationalNewsItem
from ai.ai_processing import generate_opinion
from documents.docs_generator import generate_document
import os
import dotenv

dotenv.load_dotenv()

news_url = os.getenv("NEWS_URL")
news_img_url = os.getenv("NEWS_IMG_URL")
gemini_api_key = os.getenv("GEMINI_API_KEY")
universidad = os.getenv("UNIVERSIDAD")
materia = os.getenv("MATERIA")
nombre = os.getenv("NOMBRE")
curso = os.getenv("CURSO")
profesor = os.getenv("PROFESOR")


national_news = NationalNewsItem(news_url=news_url,
                                 img_url=news_img_url)
national_news.get_news_info()


international_news = InternationalNewsItem()
international_news.get_news_info()


editorial_news = NationalNewsItem(news_url=news_url,
                                  img_url=news_img_url)
editorial_news.get_news_info()


national_news.opinion = generate_opinion(national_news.text, gemini_api_key)
international_news.opinion = generate_opinion(
    international_news.text, gemini_api_key)
editorial_news.opinion = generate_opinion(editorial_news.text, gemini_api_key)


generate_document(national_news, international_news,
                  editorial_news, universidad, materia, nombre, curso, profesor)

print("Documento generado con éxito")
