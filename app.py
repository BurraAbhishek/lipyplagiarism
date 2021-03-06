from flask import Flask, request, render_template
from conf import routes
from modules.i18n import langs_list
import json

app = Flask(__name__)

@app.context_processor
def i18n():
    try:
        lang = request.cookies.get("doclang")
    except:
        lang = "en"
    basedir = "translations/"
    try:
        destdir = basedir + "dest/site/" + lang + ".json"
        with open(destdir) as d:
            data = json.load(d)
    except:
        srcdir = basedir + "source/site.json"
        with open(srcdir) as s:
            data = json.load(s)
    return dict(i18n=data)

@app.errorhandler(404)
def not_found(e):
    return render_template(
        'oops/404.html',
        head="common/head.html", 
        appbar="common/appbar.html"
        )

@app.errorhandler(403)
def forbidden(e):
    return render_template(
        'oops/403.html',
        head="common/head.html", 
        appbar="common/appbar.html"
        )

@app.errorhandler(400)
def bad_request(e):
    return render_template(
        'oops/400.html',
        head="common/head.html", 
        appbar="common/appbar.html"
        )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template(
            'index.html', 
            inputtext="",
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template(
        'settings.html', 
        inputtext="",
        head="common/head.html", 
        appbar="common/appbar.html",
        langs_list=langs_list.langs_list
        )

@app.route('/pdfToText/', methods=['POST'])
def PDFToTextArea():
    try:
        return routes.PDFToText()
    except:
        return render_template(
            'index.html', 
            inputtext="",
            head="common/head.html", 
            appbar="common/appbar.html"
            ) 

@app.route('/about', methods=['GET'])
def about():
    return render_template(
            'docs/about.html',
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/contact', methods=['GET'])
def contact():
    return render_template(
            'docs/contact.html',
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template(
            'docs/privacy.html',
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/terms-of-service', methods=['GET'])
def tos():
    return render_template(
            'docs/tos.html',
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/source', methods=['GET'])
def source():
    return render_template(
            'docs/source.html',
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/changelog', methods=['GET'])
def changelog():
    return render_template(
            'docs/changelog.html',
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/how-to-cheat', methods=['GET'])
def cheat():
    return render_template(
            'docs/cheat.html',
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/faq', methods=['GET'])
def faq():
    return render_template(
            'docs/faq.html',
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/check-plain-text', methods=['POST'])
def check_text_initial():
    result = request.form
    return routes.checkTextInitial(result)
