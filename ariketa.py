import requests
from bs4 import BeautifulSoup
import json

class HackerNewsScrapper:
    def __init__(self, url="https://news.ycombinator.com/"):
        self.url = url
        self.albisteak = []

    def albisteakLortu(self): 
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        albisteak = soup.select(".titleline > a")
        for albistea in albisteak:
            self.albisteak.append(albistea.text)

    def fitxategiraGorde(self):
        with open("hackernews.json", "w") as hackerFitxategia:
            json.dump(self.albisteak, hackerFitxategia)

class PythonOrgScraper:
    def __init__(self, url="https://www.python.org"):
        self.url = url
        self.albisteak = []

    def albisteakLortu(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        albisteak = soup.select(".blog-widget ul.menu li a")
        for albistea in albisteak:
            self.albisteak.append(albistea.text)

    def fitxategiraGorde(self):
        with open("pythonorg.json", "w") as pythonFitxategia:
            json.dump(self.albisteak, pythonFitxategia)

class AlbisteKudeatzailea:
    def __init__(self):
        self.scrapers = []

    def scraperraGehitu(self, scraper):
        self.scrapers.append(scraper)

    def scraperrakExek(self):
        for scraper in self.scrapers:
            scraper.albisteakLortu()
            scraper.fitxategiraGorde()

if __name__ == "__main__":
    hackerNews = HackerNewsScrapper()
    pythonOrg = PythonOrgScraper()

    kudeatzailea = AlbisteKudeatzailea()
    kudeatzailea.scraperraGehitu(hackerNews)
    kudeatzailea.scraperraGehitu(pythonOrg)
    kudeatzailea.scraperrakExek()
