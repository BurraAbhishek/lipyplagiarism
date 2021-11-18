from flask import request, render_template
from modules.getText import fromPDF
from modules.plagiarism.main import calculate_plagiarism


def PDFToText():
    print('Success')
    input_file = request.files['input_text_in_file']
    output_file = fromPDF.getTextFromPDF(input_file)
    return render_template(
        'index.html', 
        inputtext=output_file,
        head="common/head.html", 
        appbar="common/appbar.html"        
        )


def checkTextInitial(text):
    print(calculate_plagiarism(text['input_text']))
    return render_template(
        'index.html', 
        inputtext=text['input_text'],
        head="common/head.html", 
        appbar="common/appbar.html"        
        )
