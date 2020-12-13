from bs4 import BeautifulSoup
import requests as req


def parse_data_from_html(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    print('Initialized soup...')

    table = soup.find('table')
    rows = table.findAll('tr')

    headers = rows[0].findAll('th')
    if headers:
        for header in headers:
            print(header.text, end=" | ")
        print()

    print("-"*10)

    for row in rows:
        cols = row.findAll('td')
        if cols:
            for col in cols:
                print(col.text, end=" | ")
            print()


# ? local: read html document
# file = open("scrap.html", 'r')
# html_doc = file.read()
# file.close()

# ? from url
response = req.get("http://python-koders-scraping.surge.sh/")

if (response.status_code == 200):
    parse_data_from_html(response.text)
else:
    print('An error occurred')
