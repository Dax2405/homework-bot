from news.national_news_item import NationalNewsItem
from news.international_news_item import InternationalNewsItem
from ai.ai_processing import generate_opinion
from documents.docs_generator import generate_document


national_news = NationalNewsItem(news_url="https://www.elcomercio.com/ultima-hora/",
                                 img_url="https://www.elcomercio.com/wp-content/uploads")
national_news.get_news_info()


international_news = InternationalNewsItem()
international_news.get_news_info()


editorial_news = NationalNewsItem(news_url="https://www.elcomercio.com/ultima-hora/",
                                  img_url="https://www.elcomercio.com/wp-content/uploads")
editorial_news.get_news_info()


national_news.opinion = generate_opinion(national_news.text)
international_news.opinion = generate_opinion(international_news.text)
editorial_news.opinion = generate_opinion(editorial_news.text)


generate_document(national_news, international_news, editorial_news)

print("Documento generado con éxito")
