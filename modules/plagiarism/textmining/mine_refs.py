import requests
from bs4 import BeautifulSoup
import warnings
from googlesearch import search
from urllib.request import Request, urlopen
from modules.plagiarism.preprocessing import preprocess

warnings.filterwarnings("ignore", module='bs4')

def getGoogleURLs(query, num_results):
    """ Get the URLs of matching documents from Google """

    urls = []
    for j in search(term=query, num_results=num_results):
        urls.append(j)
    urls.pop()
    return urls


def getAllTexts(sentence):
    texts = []
    urls = getGoogleURLs(sentence, 1)
    for i in urls:
        res = requests.get(i)
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
        texts.append(output.strip())
        return texts


#l = getAllTexts("web mining")
#for i in l:
##    s = i
#    i = preprocess.preprocess(s)
#    print(i)
#    print(' ')