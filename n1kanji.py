from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

fileName = "n1webcrap.csv"
header = "kanji, hanViet\n"
f = open(fileName, "w",  encoding="utf-8")
f.write(header)

url = "https://quizlet.com/jp/564323807/toan-bo-188-han-tu-1k-mina-no-kanji-flash-cards/"
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
web_byte = urlopen(req).read()
page_html = web_byte.decode("utf-8")
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"SetPageTerm-content"})
for container in containers:
	kanji = container.a.text
	hanViet =  container.findAll("span", {"class": "TermText notranslate lang-vi"})[0].text
	f.write(kanji + "    ,     " + hanViet+ "   \n")