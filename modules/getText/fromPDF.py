import PyPDF2

def getTextFromPDF(PDFIn):
    pdfReader = PyPDF2.PdfFileReader(PDFIn)
    s = ""
    for i in range(0, pdfReader.numPages):
        page = pdfReader.getPage(i)
        s += page.extractText()
    return PDFIn
