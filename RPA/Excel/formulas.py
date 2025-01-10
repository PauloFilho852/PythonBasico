from openpyxl import load_workbook


print('Carregando excel...')

file_name = 'Files\\read_excel.xlsx' 

wb = load_workbook(file_name)

ws1 = wb['Planilha1']

for i in range(2,5):
    nome = ws1[f'A{i}'].value
    idade = ws1[f'B{i}'].value
    print(f'{nome} tem {idade} anos.')
    

ws1['B5'].value = '=SUM(B2:B4)'

wb.save(file_name)
    