import PyPDF2
from PyPDF2.pdf import PdfFileReader

def getTextFromPDF(PDFIn):
    pdfReader = PyPDF2.PdfFileReader(PDFIn)
    s = ""
    for i in range(0, pdfReader.numPages):
        page = pdfReader.getPage(i)
        print(page)
        #s += page.extractText()
    return s


(getTextFromPDF("test.pdf"))
