from bs4 import BeautifulSoup
import requests


def box(text="*", link="*"):
    if len(text) > len(link):
        size = len(text) + 1
    else:
        size = len(link) + 1
    print(" " + "_" * size)
    print("|" + str(text) + " " * (size - len(text)) + "|")
    print("|" + str(link) + " " * (size - len(link)) + "|")
    print("|" + "_" * size + "|")
    print()


def main():
    query = input('Search for: ').strip()
    print(f'Searching for {query} ...')

    response = requests.get("https://www.bing.com/search", params={"q": query})

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find("ol", {"id": "b_results"})

        print(f"Found {len(results)} search results ....")

        links = results.findAll("li", {"class": "b_algo"})

        for item in links:
            item_text = item.find("a").text
            item_href = item.find("a").attrs["href"]

            if item_text and item_href:
                print(item_text)
                print(item_href)
                print("-"*10)


if __name__ == "__main__":
    main()
