#pip install pypdf2
from openpyxl import Workbook
import PyPDF2

pdf_file_name = 'Files\\pdf_to_excel.pdf'
xls_file_name = 'Files\\pdf_to_excel.xlsx'

print('Abrindo arquivo...')
file_reader = open(pdf_file_name, 'rb')

pdf_reader = PyPDF2.PdfReader(file_reader)

number_of_pages = len(pdf_reader.pages)

page = pdf_reader.pages[0]

page_content = page.extract_text()

file_reader.close()

page_lines = page_content.splitlines()

page_lines[0] = page_lines[0].replace('ma ', 'ma_').replace('de ', 'de_')

for i in range(0, len(page_lines)):
    page_lines[i] = page_lines[i].split(' ')
    

print('Escrevendo no Excel...')
wb = Workbook()
ws = wb.active

for line in page_lines:
    ws.append(line)

wb.save(xls_file_name)

print('Pronto.')
