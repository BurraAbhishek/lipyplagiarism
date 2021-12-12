import requests
from bs4 import BeautifulSoup

#url = 'https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/'
#url = 'https://en.wikipedia.org/wiki/Machine_Learning'

def get_text_from_url(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        'style',
        'br',
        'img',
        'footer',
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    output.replace("\n", "")
    print(output.strip())