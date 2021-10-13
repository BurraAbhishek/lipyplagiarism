from flask import Flask, request, render_template
from conf import routes

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template(
            'index.html', 
            inputtext="",
            head="common/head.html", 
            appbar="common/appbar.html"
            )

@app.route('/pdfToText/', methods=['POST'])
def PDFToTextArea():
    return routes.PDFToText()

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

@app.route('/source', methods=['GET'])
def source():
    return render_template(
            'docs/source.html',
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
