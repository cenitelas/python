import requests
from bs4 import BeautifulSoup
import sys, os
import threading
from prettytable import PrettyTable


def get_links(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    return [v['href'] for v in soup.find_all('a', href=True) if v['href'].startswith('http')]


def result_links(url, table):
    links = get_links(url)
    table.add_row([os.getpid(), len(links), url])


def main():
    print("Please wait...")
    table = PrettyTable(['PID', 'LEN', 'URL'])
    urls = sys.argv[1:]
    num_processes = len(urls)
    for index in range(num_processes):
        thread = threading.Thread(target=result_links, args=(urls[index], table))
        thread.start()
        thread.join()

    print(table)


if __name__ == '__main__':
    main()
