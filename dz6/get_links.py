import requests
from bs4 import BeautifulSoup
import sys, os
import threading


def get_links(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    return [v['href'] for v in soup.find_all('a', href=True) if v['href'].startswith('http')]


def result_links(urls):
    for url in urls:
        links = get_links(url)
        print(os.getpid(), len(links), url)


def main():
    num_processes = int(sys.argv[1])
    urls = sys.argv[2:]
    threads = list()
    for index in range(num_processes):
        thread = threading.Thread(target=result_links, args=urls)
        threads.append(thread)
        thread.start()


if __name__ == '__main__':
    main()
