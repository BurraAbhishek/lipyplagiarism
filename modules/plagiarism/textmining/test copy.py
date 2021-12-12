from urllib import request
from bs4 import BeautifulSoup as bs
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
    urls = getGoogleURLs(sentence, 3)
    for i in urls:
        req = Request(
            i,
            headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
            )
        htmlPage = urlopen(req)
        soup = bs(htmlPage, "html.parser")
        text = soup.get_text(separator="\r\n")
        texts.append(text)
    return texts


l = getAllTexts("web mining")
for i in l:
    s = i
    i = preprocess.preprocess(s)
print(str(l))