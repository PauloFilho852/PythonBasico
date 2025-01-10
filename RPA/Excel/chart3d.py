from openpyxl import Workbook
from openpyxl.chart import AreaChart3D, Reference, Series


file_name = 'Files\\Chart3D.xlsx'
wb = Workbook()
ws = wb.active

rows = [
    ['Ano', 'Lucros', 'Custos'],
    [2015, 30, 40],
    [2016, 25, 40],
    [2017, 30, 50],
    [2018, 10, 30],
    [2019, 5, 25],
    [2020, 10, 50]
]


for row in rows:
    ws.append(row)

chart = AreaChart3D()

chart.title = 'Lucros x Custos'
chart.style = 13
chart.x_axis.title = 'Ano'
chart.y_axis.title = 'Porcentagem'

categories = Reference(ws, min_col= 1, min_row=1, max_row=7)

data = Reference(ws, min_col=2, min_row=1, max_col= 3, max_row=7)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, 'A10')

wb.save(file_name)