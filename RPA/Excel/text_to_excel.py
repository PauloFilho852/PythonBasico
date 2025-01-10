from openpyxl import Workbook

txt_file_name = 'Files\\text_to_excel.txt'
xls_file_name = 'Files\\text_to_excel.xlsx'

print('Iniciando nosso robô...')

print('Lendo dados do arquivo de texto...')

file_reader = open(txt_file_name, 'r', encoding='utf8')

file_content = file_reader.read()

file_reader.close()

dados = file_content.splitlines()


for i in range(0, len(dados)):
   dados[i] = dados[i].split(',')   

   
print('Criando arquivo excel..')
wb = Workbook()
ws = wb.active

for linha in dados:
    ws.append(linha)


wb.save(xls_file_name)

print('Pronto.')