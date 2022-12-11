from openpyxl import load_workbook
import classes

book = load_workbook('Website_data.xlsx')
sheet = book.active
rows = sheet.rows
header = [cell.value for cell in next(rows)]


All_The_Data = []
for row in range(74):
    header = [cell.value for cell in next(rows)]
    All_The_Data.append(header)

for i in range(len(All_The_Data)):
    print(All_The_Data[i][10])
