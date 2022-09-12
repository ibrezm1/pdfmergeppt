import os
from PyPDF2 import PdfFileMerger

#https://stackoverflow.com/questions/3444645/merge-pdf-files

x = [a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfFileMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)