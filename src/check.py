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


Data_Sorted = []
temp_name = All_The_Data[0][10]
bigger_Data_sorted = []

for i in range(len(All_The_Data)):
    print(temp_name == All_The_Data[i][10])
    if(temp_name == All_The_Data[i][10]):
        Data_Sorted.append(All_The_Data[i])
    else:
        temp_name = (All_The_Data[i][10])
        print(temp_name)
        bigger_Data_sorted.append(Data_Sorted)
        Data_Sorted = []
        Data_Sorted.append(All_The_Data[i])
bigger_Data_sorted.append(Data_Sorted)

allvars = vars()
for i in range(len(bigger_Data_sorted)):
    floorlist=[]
    for j in range(len(bigger_Data_sorted[i])):
        x = 1
        floorlist.append(Floor(bigger_Data_sorted[i][j][7],bigger_Data_sorted[i][j][6],bigger_Data_sorted[i][j][5]))
    #print(bigger_Data_sorted[0][0][10])
    allvars[bigger_Data_sorted[i][0][10]] = Building(floorlist,bigger_Data_sorted[i][0][4],bigger_Data_sorted[i][0][1],bigger_Data_sorted[i][0][2],bigger_Data_sorted[i][0][0],bigger_Data_sorted[i][0][3])

print(Yawkey.buildingname)




