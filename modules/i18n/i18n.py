import json

lang = "fr-FR"

basedir = "translations/"
try:
    destdir = basedir + "dest/site/" + lang + ".json"
    with open(destdir) as d:
        data = json.load(d)
except:
    srcdir = basedir + "source/site.json"
    with open(srcdir) as s:
        data = json.load(s)

def i18n(s):
    return data[s]
