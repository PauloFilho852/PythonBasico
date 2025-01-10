from openpyxl import Workbook

wb = Workbook()

file_name = 'Files\\write_excel.xlsx'

ws1 = wb.active
ws1.title = 'MinhaPlanilha1'

dados = [
    ['Ano', 'Lucro', 'Custos'],
    [2015, '30%', '40%'],
    [2016, '50%', '40%'],
    [2017, '70%', '40%']
    ]


for linha in dados:
    ws1.append(linha)

ws2 = wb.create_sheet(title='MinhaPlanilha2')

ws2['F5'].value = 3.14

print(ws2['F5'].value)

wb.save(file_name)