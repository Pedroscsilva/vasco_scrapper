import requests
from bs4 import BeautifulSoup

url = "https://www.supervasco.com/"
page = requests.get(url)
html_content = page.text

soup = BeautifulSoup(html_content, "html.parser")

page_titles = soup.select("h4 a").attrs

for title in page_titles:
    print(title.attrs)
