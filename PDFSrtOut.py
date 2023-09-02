from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz
from pandas import *

data = read_csv("NameFile.csv")

addrs = data['address'].tolist()
nme = data['name'].tolist()
i = 0
while i < len(addrs):
    filename = "MainPDF.pdf"
    filename_sub = filename.replace('.pdf', '')
    while True:
        pdf_document = fitz.open(filename)
        pages = []
        for current_page in range(len(pdf_document)):
            page = pdf_document.load_page(current_page)
            if page.search_for(addrs[i]):
                pages.append(current_page)
                print(f"{addrs[i]} found on page {current_page+1}")
        if not pages:
            #exit()
            print(f"{addrs[i]} not found")
        pdf = PdfFileReader(filename)
        pdfWriter = PdfFileWriter()
        for page_num in pages:
            pdfWriter.addPage(pdf.getPage(page_num))

        with open(f"{nme[i]}.pdf", 'wb') as f:
            pdfWriter.write(f)
            f.close()
            break
    i = i + 1
