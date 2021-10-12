import pdftotext

def getTextFromPDF(PDFIn):
    with open(PDFIn, 'rb') as f:
        pdf = pdftotext.PDF(f)
    s = "\n\n".join(pdf)
    return s