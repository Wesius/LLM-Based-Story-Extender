import requests
from bs4 import BeautifulSoup
import os

def create_directories():
    os.makedirs('chapters', exist_ok=True)


def get_chapter_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    chapter_links = []
    # Find and extract chapter links from the table
    # You'll need to inspect the HTML structure and adjust the selector
    for link in soup.select('table#chapters a'):
        chapter_links.append(link['href'])
    # delete duplicate links
    chapter_links = list(dict.fromkeys(chapter_links))
    return chapter_links


def download_chapter(url, chapter_number):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract the chapter content
    # You'll need to inspect the HTML structure and adjust the selector
    chapter_content = soup.select_one('div.chapter-inner').text

    # Save the chapter content to a file
    with open(f'chapters/chapter_{chapter_number}.txt', 'w', encoding='utf-8') as f:
        f.write(chapter_content)


def main():
    create_directories()
    base_url = 'https://www.royalroad.com'
    fiction_url = f'{base_url}/fiction/75057/manifest-fantasy'

    chapter_links = get_chapter_links(fiction_url)

    for i, link in enumerate(chapter_links, 1):
        full_url = base_url + link
        print(f'Downloading Chapter {i}...')
        download_chapter(full_url, i)
        print(f'Chapter {i} downloaded.')


if __name__ == '__main__':
    main()