# Python OOP Soila

Proiektu honek Python erabiliz web scraping sinplea egiten du, HN (Hacker News) eta Python.org-en albisteak ateratzen ditu, eta JSON fitxategi batean gordetzen ditu.

## Deskribapena

Klasikoki, proiektua objektuetara bideratutako programazioaren (OOP) adibide gisa diseinatuta dago. Hiru klase nagusi daude:

- `HackerNewsScrapper`: Hacker News-eko tituluak lortzen ditu.
- `PythonOrgScraper`: Python.org-eko blogeko estekak lortzen ditu.
- `AlbisteKudeatzailea`: scraper guztiak kudeatu eta exekutatzen ditu.

## Nola funtzionatzen du

Programa `if __name__ == "__main__":` blokean exekutatzen da. Bertan:

1. `HackerNewsScrapper` instantzia sortzen da.
2. `PythonOrgScraper` instantzia sortzen da.
3. Bi scraperrak `AlbisteKudeatzailea` objektuaren bidez gehitzen dira.
4. `scraperrakExek()` metodoak datuak eskuratu eta JSON fitxategitan gordetzen ditu.

## Sortutako fitxategiak

- `hackernews.json`: Hacker News-eko tituluak gordetzeko fitxategia.
- `pythonorg.json`: Python.org-eko albisteen izenak gordetzeko fitxategia.

## Esker zerrenda

Proiektu hau exekutatzeko beharrezkoa da Python ingurunea eta `requests` eta `beautifulsoup4` liburutegiak instalatzea.

```bash
pip install requests beautifulsoup4
```

Ondoren, script-a exekutatu:

```bash
python ariketa.py
```

## Oharrak

- Proiektua erakustaldi edo praktikaren adibide gisa sortu da.
- Web scraping-a zerbitzariaren webguneen baldintzei men eginda egitea beharrezkoa da.
- Erabilera kontrolatua eta arduratsua gomendatzen da.

## LICENSE

Proiektuan ez dago licentziarik adierazituta, beraz, erabilera eta banaketa kontuan edukitzea gomendatzen da.
