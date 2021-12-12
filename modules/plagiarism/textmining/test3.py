import requests
from bs4 import BeautifulSoup

url = 'http://www.africau.edu/images/default/sample.pdf'
res = requests.get(url)
if "text/html" in res.headers["content-type"]:
    html = res.text
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
