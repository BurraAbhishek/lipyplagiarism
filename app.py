from flask import Flask, request, render_template
from conf import routes

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', inputtext="")

@app.route('/pdfToText/', methods=['POST'])
def PDFToTextArea():
    return routes.PDFToText()
