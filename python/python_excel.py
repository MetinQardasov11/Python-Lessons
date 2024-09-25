from openpyxl import Workbook
from openpyxl.styles import Font
from random import randint
import names

wb = Workbook()
ws = wb.active

students = [[names.get_full_name(), randint(1,10), randint(10,20), randint(10,20)] for x in range(25)]

data_title = [['Student Name', 'Activity', 'Presentation', 'Midterm'], * students]

for row in data_title:
    ws.append(row)
    
    
ft = Font(bold=True, color='00FF0000')
for row in ws['A1:D1']:
    for cell in row:
        cell.font = ft


ws.column_dimensions['A'].width = 20
wb.save("xlsx/student.xlsx")