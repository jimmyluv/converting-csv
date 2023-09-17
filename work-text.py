import PyPDF2
pdf_file = open('movie-data.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

with open('output.txt', 'w', encoding= 'utf 8') as text_file:

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        text_file.write(text)
pdf_file.close


