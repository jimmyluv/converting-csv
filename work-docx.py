from pdf2docx import Converter

# convert PDF to docx
cv = Converter('movie-data.pdf')
cv.convert('input.docx', start=0, end=None)
cv.close