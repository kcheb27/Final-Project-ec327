from openpyxl import load_workbook
from classes import Floor
from classes import Building

book = load_workbook('Website_data.xlsx')
sheet = book.active
rows = sheet.rows
header = [cell.value for cell in next(rows)]


All_The_Data = []
for row in range(74):
    header = [cell.value for cell in next(rows)]
    All_The_Data.append(header)

print(All_The_Data[0][10])

allvars = vars()
floorlist = []
i = 0
while i< len(All_The_Data):
    floorlist.clear()
    count = 1
    current_name = All_The_Data[i][10]
    floorlist.append(Floor(All_The_Data[i][7],All_The_Data[i][6], All_The_Data[i][5]))
    while current_name == All_The_Data[i+count][10]:
        count+=1
        if (i+count) == len(All_The_Data):
            count -= 1
            current_name == ""
        else:
            floorlist.append(Floor(165,200,1)) #Floor(All_The_Data[i+count][7],All_The_Data[i+count][6], All_The_Data[i+count][5])
    current_name = All_The_Data[i][10]
    allvars[current_name]  = Building(floorlist,All_The_Data[i][7], All_The_Data[i][1],All_The_Data[i][2],All_The_Data[i][0],All_The_Data[i][3])      
    i += count


print(StuVi1.buildingname)

teststring = All_The_Data[0][10]
floor_list13 = [Floor(165,200,1),Floor(185,200,2)]
allvars[teststring] = Building(floor_list13,9,"Dorm","N/a","The Towers","140 Bay State Road")
print(StuVi1.buildingname)