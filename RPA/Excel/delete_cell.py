from openpyxl import load_workbook

file_name = 'Files\\delete_cell.xlsx'

wb = load_workbook(file_name)

ws = wb['Data']

ws.delete_rows(1,3) #Apaga as linhas de 1 a 3
ws.delete_cols(1,3) #Apaga as colunas de 1 a 3

wb.save(file_name)