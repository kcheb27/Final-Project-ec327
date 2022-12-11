from openpyxl import load_workbook
from classes import Floor
from classes import Building
book = load_workbook('Website_data.xlsx')
sheet = book.active
rows = sheet.rows
header = [cell.value for cell in next(rows)]


All_The_Data = []
print(header)
for row in range(74):
    header = [cell.value for cell in next(rows)]
    All_The_Data.append(header)

print(len(All_The_Data))


teststring = "ISEX"
allvars = vars()
floor_list13 = [Floor(165,200,1),Floor(185,200,2)]
allvars[teststring] = Building(floor_list13,9,"Dorm","N/a","The Towers","140 Bay State Road")
print(ISEX.buildingname)