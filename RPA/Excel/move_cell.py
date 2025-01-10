from openpyxl import load_workbook

file_name = 'Files\\move_cell.xlsx'

wb = load_workbook(file_name)

ws = wb['Data']

#Linhas: negativo para cima. Colunas: Negativo para esquerda.

#Move a linha 2, de A a Z, um linha para cima.
ws.move_range('A2:Z2', rows= -1)

#Move a célula F8 duas célula para esqueda.
ws.move_range('F8', cols = -2)

#Move a célula F10 duas células para direita.
ws.move_range('D10', cols = 2)

#Move a faixa indicada duas colunas, dentro da faixa, para esqueda e uma linha, dentro da faixa, para cima.
ws.move_range('C13:E15', cols = -2, rows= -1)
wb.save(file_name)