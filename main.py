from flask import Flask,render_template
from classes import Floor
from classes import Building
from openpyxl import load_workbook
import os

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

    if(temp_name == All_The_Data[i][10]):
        Data_Sorted.append(All_The_Data[i])
    else:
        temp_name = (All_The_Data[i][10])
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

app = Flask(__name__)
picFolder = os.path.join('static','pics')


app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'THEHAND.jpg')
    return render_template("index.html",name ="Tim",image =pic1,Page = "Home Page",image2 = pic2)

@app.route("/unhinged")
def home2():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'betterbetterbulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'betterbulogo.png')
    return render_template("unhinged.html",name ="Tim",image =pic1,Page = "IGGGGGGGGGYYYYYY",image2 = pic2)    

floornumber = []
floorcap = []
floorpop = []
#####################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Gsu.no_floors_study):
    floornumber.append(Gsu.floor_study[x].level)
    floorcap.append(Gsu.floor_study[x].capacity)
    floorpop.append(StuVi1.floor_study[x].population)

@app.route("/GSU")
def gsu():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'gsu.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Gsu.buildingname,capacity = Gsu.capacity,population = Gsu.population,number_floors = Gsu.no_floor, \
    number_studyfloors = Gsu.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Gsu.type,subtype = Gsu.subtype,address = Gsu.address)
############################# THE TRUTH##################################


###############################EVERYTHING ELSE CAN GO DIE#################################################


@app.route("/StuVi1")
def stuvi1():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,StuVi1.no_floors_study):
        floornumber.append(StuVi1.floor_study[x].level)
        print(StuVi1.floor_study[x].level)
        floorcap.append(StuVi1.floor_study[x].capacity)
        print(StuVi1.floor_study[x].capacity)
        floorpop.append(StuVi1.floor_study[x].population)
        print(StuVi1.floor_study[x].population)

    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'StuVi1.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = StuVi1.buildingname,capacity = StuVi1.capacity, \
    population = StuVi1.population,number_floors = StuVi1.no_floor,number_studyfloors = StuVi1.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = StuVi1.type,subtype = StuVi1.subtype,address = StuVi1.address)
###################################################################################################################


@app.route("/Metcalf")
def metcalf():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Metcalf.no_floors_study):
        floornumber.append(Metcalf.floor_study[x].level)
        floorcap.append(Metcalf.floor_study[x].capacity)
        floorpop.append(Metcalf.floor_study[x].population)
        pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
        pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Metcalf.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Metcalf.buildingname,capacity = Metcalf.capacity, \
    population = Metcalf.population,number_floors = Metcalf.no_floor,number_studyfloors = Metcalf.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Metcalf.type,subtype = Metcalf.subtype,address = Metcalf.address)
##########################################################################################################################

@app.route("/Photonics")
def photonics():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Photonics.no_floors_study):
        floornumber.append(Photonics.floor_study[x].level)
        floorcap.append(Photonics.floor_study[x].capacity)
        floorpop.append(Photonics.floor_study[x].population)
        pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
        pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Photonics.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Photonics.buildingname,capacity = Photonics.capacity, \
    population = Photonics.population,number_floors = Photonics.no_floor,number_studyfloors = Photonics.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Photonics.type,subtype = Photonics.subtype,address = Photonics.address)
##############################################################################################################################

@app.route("/Wheelock")
def wheelock():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Wheelock.no_floors_study):
        floornumber.append(Wheelock.floor_study[x].level)
        floorcap.append(Wheelock.floor_study[x].capacity)
        floorpop.append(Wheelock.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Wheelock.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Wheelock.buildingname,capacity = Wheelock.capacity, \
    population = Wheelock.population,number_floors = Wheelock.no_floor,number_studyfloors = Wheelock.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Wheelock.type,subtype = Wheelock.subtype,address = Wheelock.address)
##################################################################################################################################

@app.route("/Yawkey")
def yawkey():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Yawkey.no_floors_study):
        floornumber.append(Yawkey.floor_study[x].level)
        floorcap.append(Yawkey.floor_study[x].capacity)
        floorpop.append(Yawkey.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Yawkey.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Yawkey.buildingname,capacity = Yawkey.capacity, \
    population = Yawkey.population,number_floors = Yawkey.no_floor,number_studyfloors = Yawkey.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Yawkey.type,subtype = Yawkey.subtype,address = Yawkey.address)
#################################################################################################################################

@app.route("/Howard_Therman_Center")
def htc():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Howard_Therman_Center.no_floors_study):
        floornumber.append(Howard_Therman_Center.floor_study[x].level)
        floorcap.append(Howard_Therman_Center.floor_study[x].capacity)
        floorpop.append(Howard_Therman_Center.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Howard_Therman_Center.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Howard_Therman_Center.buildingname,capacity = Howard_Therman_Center.capacity, \
    population = Howard_Therman_Center.population,number_floors = Howard_Therman_Center.no_floor,number_studyfloors = Howard_Therman_Center.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Howard_Therman_Center.type,subtype = Howard_Therman_Center.subtype,address = Howard_Therman_Center.address)
#####################################################################################################################################

@app.route("/Cas")
def cas():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Cas.no_floors_study):
        floornumber.append(Cas.floor_study[x].level)
        floorcap.append(Cas.floor_study[x].capacity)
        floorpop.append(Cas.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Cas.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Cas.buildingname,capacity = Cas.capacity, \
    population = Cas.population,number_floors = Cas.no_floor,number_studyfloors = Cas.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Cas.type,subtype = Cas.subtype,address = Cas.address)
############################################################################################################################################

@app.route("/Cfa")
def cfa():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Cfa.no_floors_study):
        floornumber.append(Cfa.floor_study[x].level)
        floorcap.append(Cfa.floor_study[x].capacity)
        floorpop.append(Cfa.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'cfa.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Cfa.buildingname,capacity = Cfa.capacity, \
    population = Cfa.population,number_floors = Cfa.no_floor,number_studyfloors = Cfa.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Cfa.type,subtype = Cfa.subtype,address = Cfa.address)
############################################################################################################################################

@app.route("/Cgs")
def cgs():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Cgs.no_floors_study):
        floornumber.append(Cgs.floor_study[x].level)
        floorcap.append(Cgs.floor_study[x].capacity)
        floorpop.append(Cgs.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'cgs.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Cgs.buildingname,capacity = Cgs.capacity, \
    population = Cgs.population,number_floors = Cgs.no_floor,number_studyfloors = Cgs.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Cgs.type,subtype = Cgs.subtype,address = Cgs.address)
############################################################################################################################################

@app.route("/Com")
def com():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Com.no_floors_study):
        floornumber.append(Com.floor_study[x].level)
        floorcap.append(Com.floor_study[x].capacity)
        floorpop.append(Com.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'com.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Com.buildingname,capacity = Com.capacity, \
    population = Com.population,number_floors = Com.no_floor,number_studyfloors = Com.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Com.type,subtype = Com.subtype,address = Com.address)
############################################################################################################################################

@app.route("/Epic")
def epic():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Epic.no_floors_study):
        floornumber.append(Epic.floor_study[x].level)
        floorcap.append(Epic.floor_study[x].capacity)
        floorpop.append(Epic.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'epic.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Epic.buildingname,capacity = Epic.capacity, \
    population = Epic.population,number_floors = Epic.no_floor,number_studyfloors = Epic.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Epic.type,subtype = Epic.subtype,address = Epic.address)
############################################################################################################################################

@app.route("/Rich")
def rich():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Rich.no_floors_study):
        floornumber.append(Rich.floor_study[x].level)
        floorcap.append(Rich.floor_study[x].capacity)
        floorpop.append(Rich.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'RichHall.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Rich.buildingname,capacity = Rich.capacity, \
    population = Rich.population,number_floors = Rich.no_floor,number_studyfloors = Rich.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Rich.type,subtype = Rich.subtype,address = Rich.address)
############################################################################################################################################

@app.route("/Sleeper")
def sleeper():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Sleeper.no_floors_study):
        floornumber.append(Sleeper.floor_study[x].level)
        floorcap.append(Sleeper.floor_study[x].capacity)
        floorpop.append(Sleeper.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Sleeper.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Sleeper.buildingname,capacity = Sleeper.capacity, \
    population = Sleeper.population,number_floors = Sleeper.no_floor,number_studyfloors = Sleeper.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Sleeper.type,subtype = Sleeper.subtype,address = Sleeper.address)
############################################################################################################################################

@app.route("/Claflin")
def claflin():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Claflin.no_floors_study):
        floornumber.append(Claflin.floor_study[x].level)
        floorcap.append(Claflin.floor_study[x].capacity)
        floorpop.append(Claflin.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Claflin.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Claflin.buildingname,capacity = Claflin.capacity, \
    population = Claflin.population,number_floors = Claflin.no_floor,number_studyfloors = Claflin.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Claflin.type,subtype = Claflin.subtype,address = Claflin.address)
############################################################################################################################################

@app.route("/TenNineteen")
def tennineteen():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,TenNineteen.no_floors_study):
        floornumber.append(TenNineteen.floor_study[x].level)
        floorcap.append(TenNineteen.floor_study[x].capacity)
        floorpop.append(TenNineteen.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'TenNineteen.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = TenNineteen.buildingname,capacity = TenNineteen.capacity, \
    population = TenNineteen.population,number_floors = TenNineteen.no_floor,number_studyfloors = TenNineteen.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = TenNineteen.type,subtype = TenNineteen.subtype,address = TenNineteen.address)
############################################################################################################################################

@app.route("/Warren")
def warren():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Warren.no_floors_study):
        floornumber.append(Warren.floor_study[x].level)
        floorcap.append(Warren.floor_study[x].capacity)
        floorpop.append(Warren.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Warrentowers.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Warren.buildingname,capacity = Warren.capacity, \
    population = Warren.population,number_floors = Warren.no_floor,number_studyfloors = Warren.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Warren.type,subtype = Warren.subtype,address = Warren.address)
############################################################################################################################################

@app.route("/Towers")
def towers():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Towers.no_floors_study):
        floornumber.append(Towers.floor_study[x].level)
        floorcap.append(Towers.floor_study[x].capacity)
        floorpop.append(Towers.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Towers.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Towers.buildingname,capacity = Towers.capacity, \
    population = Towers.population,number_floors = Towers.no_floor,number_studyfloors = Towers.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Towers.type,subtype = Towers.subtype,address = Towers.address)
############################################################################################################################################

@app.route("/Myles")
def myles():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Myles.no_floors_study):
        floornumber.append(Myles.floor_study[x].level)
        floorcap.append(Myles.floor_study[x].capacity)
        floorpop.append(Myles.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'MylesStandishHall.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Myles.buildingname,capacity = Myles.capacity, \
    population = Myles.population,number_floors = Myles.no_floor,number_studyfloors = Myles.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Myles.type,subtype = Myles.subtype,address = Myles.address)
############################################################################################################################################

@app.route("/Kilachand")
def kilachand():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Kilachand.no_floors_study):
        floornumber.append(Kilachand.floor_study[x].level)
        floorcap.append(Kilachand.floor_study[x].capacity)
        floorpop.append(Kilachand.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Kilachand_Hall.jpeg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Kilachand.buildingname,capacity = Kilachand.capacity, \
    population = Kilachand.population,number_floors = Kilachand.no_floor,number_studyfloors = Kilachand.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Kilachand.type,subtype = Kilachand.subtype,address = Kilachand.address)
############################################################################################################################################

@app.route("/Danielsen")
def danielsen():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Danielsen.no_floors_study):
        floornumber.append(Danielsen.floor_study[x].level)
        floorcap.append(Danielsen.floor_study[x].capacity)
        floorpop.append(Danielsen.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'DanielsenHall.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Danielsen.buildingname,capacity = Danielsen.capacity, \
    population = Danielsen.population,number_floors = Danielsen.no_floor,number_studyfloors = Danielsen.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Danielsen.type,subtype = Danielsen.subtype,address = Danielsen.address)
############################################################################################################################################

@app.route("/Mugar")
def mugar():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Mugar.no_floors_study):
        floornumber.append(Mugar.floor_study[x].level)
        floorcap.append(Mugar.floor_study[x].capacity)
        floorpop.append(Mugar.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Mugar.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Mugar.buildingname,capacity = Mugar.capacity, \
    population = Mugar.population,number_floors = Mugar.no_floor,number_studyfloors = Mugar.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Mugar.type,subtype = Mugar.subtype,address = Mugar.address)
############################################################################################################################################

@app.route("/Lse")
def lse():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Lse.no_floors_study):
        floornumber.append(Lse.floor_study[x].level)
        floorcap.append(Lse.floor_study[x].capacity)
        floorpop.append(Lse.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Lse.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Lse.buildingname,capacity = Lse.capacity, \
    population = Lse.population,number_floors = Lse.no_floor,number_studyfloors = Lse.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Lse.type,subtype = Lse.subtype,address = Lse.address)
############################################################################################################################################

@app.route("/Questrom")
def questrom():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Questrom.no_floors_study):
        floornumber.append(Questrom.floor_study[x].level)
        floorcap.append(Questrom.floor_study[x].capacity)
        floorpop.append(Questrom.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Questrom.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Questrom.buildingname,capacity = Questrom.capacity, \
    population = Questrom.population,number_floors = Questrom.no_floor,number_studyfloors = Questrom.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Questrom.type,subtype = Questrom.subtype,address = Questrom.address)
############################################################################################################################################

@app.route("/Law")
def law():
    floornumber.clear()
    floorcap.clear()
    floorpop.clear()
    for x in range(0,Law.no_floors_study):
        floornumber.append(Law.floor_study[x].level)
        floorcap.append(Law.floor_study[x].capacity)
        floorpop.append(Law.floor_study[x].population)
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Law.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Law.buildingname,capacity = Law.capacity, \
    population = Law.population,number_floors = Law.no_floor,number_studyfloors = Law.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Law.type,subtype = Law.subtype,address = Law.address)
