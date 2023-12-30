import requests
from bs4 import BeautifulSoup

basic_url = "https://www.supervasco.com"


def get_all_news():
    page = requests.get(basic_url)
    html_content = page.text

    soup = BeautifulSoup(html_content, "html.parser")

    page_titles = soup.select("h4 a")

    page_attrs = map(lambda title: title.attrs, page_titles)

    return list(page_attrs)


def get_specific_new(additional_href):
    page = requests.get(f"{basic_url}{additional_href}")
    html_content = page.text

    soup = BeautifulSoup(html_content, "html.parser")

    page_title = soup.select_one("h1").text
    page_text_html = soup.select("#lightgallery > p")

    print(f"\n{page_title}\n")
    for html in page_text_html:
        if html.text != "":
            print(html.text)
