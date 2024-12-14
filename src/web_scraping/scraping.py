from bs4 import BeautifulSoup as bs
import requests
import json


def ger_url_content(url):
    response = requests.get(url)
    return response.text


def get_soup(url):
    try:
        content = ger_url_content(url)
        soup = bs(content, "html.parser")
        return soup
    except Exception as e:
        print(e)
        return None
