from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import argparse


def pdf2xt(path):
    """
    Extract text from PDF file, and return
    the string contained inside
    :param path (str) path to the .pdf file
    :return: text (str) string extracted
    """

    rsrcmgr = PDFResourceManager()
    retstr = BytesIO()
    device = TextConverter(rsrcmgr, retstr)
    with open(path, "rb") as fp:  # open in 'rb' mode to read PDF bytes
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, check_extractable=True):
            interpreter.process_page(page)
        device.close()
        text = retstr.getvalue()
        retstr.close()
    return text


if __name__ == '__main__':
    # ARGUMENTS FOR THE EXTRACTOR
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-s", "--source", required=True, help="path to input .pdf to be converted")
    argparser.add_argument("-f", "--file", required=False, help="path to the ouput .txt file")
    args = vars(argparser.parse_args())
    source = args["source"]
    file = args["file"]

    # EXTRACTING TEXT
    print('-- Extracting')
    pdf_text = pdf2xt(source)
    print('-- Output: {}'.format(pdf_text))

    # SAVING TEXT IN .TXT FILE
    if file:
        print('-- Writing file')
        with open(file, "wb") as f:
            f.write(pdf_text)
        print('-- File written here: {}'.format(file))