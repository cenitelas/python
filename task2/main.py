import requests
from bs4 import BeautifulSoup
import sys


def get_links(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    return [v['href'] for v in soup.find_all('a', href=True) if v['href'].startswith('http')]


def main():
    url = sys.argv[1]
    try:
        print(f"{len(get_links(url))} {url}")
    except Exception as e:
        try:
            print(f"{len(get_links(f'http://{url}'))} {url}")
        except Exception as e:
            print("Ошибка адреса")


if __name__ == '__main__':
    main()

