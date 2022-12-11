from flask import Flask,render_template
from classes import Floor
from classes import Building
import os

#example Building make: StuVi 1
#implement the objects into the initialization of a model class
floor_list1 = [Floor(10,20,1),Floor(10,30,2),Floor(30,80,26)]
StuVi1 = Building(floor_list1,26,"Dorm","N/a","StuVi1","33 Harry Agganis Way")

floor_list2 = [Floor(38,40,0),Floor(19,20,1),Floor(18,20,2),Floor(8,10,3)]
Metcalf = Building(floor_list2,3,"School","N/a","Metcalf","1 Silber Way")

floor_list3 = [Floor(12,60,1),Floor(23,40,2),Floor(12,30,3,),Floor(8,20,4),Floor(7,20,5),Floor(15,20,6),Floor(12,20,7)]
Photonics = Building(floor_list3,9,"School","N/a","Photonics","8 St. Mary's Street")

floor_list4 = [Floor(16,30,1),Floor(18,30,2)]
Wheelock = Building(floor_list4,3,"School","N/a","Wheelock","2 Silber Way")

floor_list5 = [Floor(9,10,1),Floor(0,10,2),Floor(23,40,3),Floor(13,30,4),Floor(15,30,5),Floor(19,30,6)]
Yawkey = Building(floor_list5,6,"School","Food","Yawkey","100 Bay State Road")


floor_list13 = [Floor(165,200,1),Floor(185,200,2)]
Howard_Therman_Center = Building(floor_list13, 5, "Study", "N/a", "Howard Therman Center", "808 Commonwealth Ave")
floor_list14 = [Floor(35,50,0),Floor(18,30,1), Floor(12,30,2),Floor(8,20,3),Floor(7,30,4),Floor(9,20,5)]
Cas = Building(floor_list14, 5, "School", "N/a", "CAS", "725 Commonwealth Ave")
floor_list15 = [Floor(45,80,1),Floor(22,40,2), Floor(18,30,3)]
Cfa = Building(floor_list15,5,"School","N/a","CFA", "855 Commonwealth Ave")
floor_list16 = [Floor(22,40,1),Floor(18,30,2), Floor(11,20,3)]
Cgs = Building(floor_list16,4, "School","N/a","CGS","871 Commonwealth Ave")
floor_list17 = [Floor(18,30,1),Floor(22,40,2)]
Com = Building(floor_list17, 3, "School","N/a","COM","640 Commonwealth Ave")
floor_list18 = [Floor(6,10,1),Floor(65,100,2)]
Epic = Building(floor_list18, 2, "School", "N/a", "EPIC", "750 Commonwealth Ave")

floor_list_rich = [Floor(47,80,1)]
Rich = Building(floor_list_rich,13,"Dorm","N/a","Rich Hall","277 Babcock Street")

floor_list_sleeper = [Floor(12,30,2)]
Sleeper = Building(floor_list_sleeper,13,"Dorm","N/a","Sleeper Hall","275 Babcock Street")

floor_list_claflin = [Floor(18,30,1)]
Claflin = Building(floor_list_claflin,13,"Dorm","N/a","Claflin Hall","273 Babcock Street")

floor_list_1019 = [Floor(8,20,2)]
TenNineteen = Building(floor_list_1019,6,"Dorm","N/a","1019 Commonwealth Ave","1019 Commonwealth Avenue")

floor_list_warren = [Floor(37,40,4)]
Warren = Building(floor_list_warren,18,"Dorm","Food","Warren Towers","700 Commonwealth Avenue")

floor_list_towers = [Floor(28,30,1),Floor(38,40,2)]
Towers = Building(floor_list_towers,9,"Dorm","N/a","The Towers","140 Bay State Road")

floor_list_myles = [Floor(9,20,1)]
Myles = Building(floor_list_myles,9,"Dorm","N/a","Myles Standish Hall","610 Beacon Street")

floor_list_kilachand = [Floor(45,75,1)]
Kilachand = Building(floor_list_kilachand,9,"Dorm","N/a","Kilachand Hall","91 Bay State Road")

floor_list_danielsen = [Floor(17,20,1)]
Danielsen = Building(floor_list_danielsen,10,"Dorm","N/a","Danielsen Hall","512 Beacon Street")

floor_list_mugar = [Floor(85,115,1),Floor(198,206,2),Floor(65,80,3),Floor(55,80,4),Floor(28,50,5),Floor(18,40,6)]
Mugar = Building(floor_list_mugar,6,"Library","N/a","Mugar Library","771 Commonwealth Avenue")

floor_list_gsu = [Floor(145,250,1),Floor(78,125,2),Floor(80,60,3)]
Gsu = Building(floor_list_gsu,3,"Food","Study","George Sherman Union","775 Commonwealth Avenue")

floor_list21=[Floor(37,80,1),Floor(3,20,2),Floor(9,20,3)]
Lse = Building(floor_list21,3,"School","N/a","LSE","24 Cummington Mall")

floor_list_questrom=[Floor(62,80,1),Floor(63,100,2),Floor(79,150,3),Floor(26,40,4),Floor(9,20,5),Floor(0,20,6),Floor(23,150,7)]
Questrom = Building(floor_list_questrom,7,"School","N/a","Questrom School of Business","595 Commonwealth Avenue")

floor_list_law = [Floor(12,60,1),Floor(89,100,2),Floor(49,150,3),Floor(63,50,4),Floor(4,20,5)]
Law = Building(floor_list_law,16,"School","N/a","Law Building","765 Commonwealth Avenue")

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
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,StuVi1.no_floors_study):
    floornumber.append(StuVi1.floor_study[x].level)
    floorcap.append(StuVi1.floor_study[x].capacity)
    floorpop.append(StuVi1.floor_study[x].population)

@app.route("/StuVi1")
def stuvi1():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'StuVi1.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = StuVi1.buildingname,capacity = StuVi1.capacity, \
    population = StuVi1.population,number_floors = StuVi1.no_floor,number_studyfloors = StuVi1.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = StuVi1.type,subtype = StuVi1.subtype,address = StuVi1.address)
###################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Metcalf.no_floors_study):
    floornumber.append(Metcalf.floor_study[x].level)
    floorcap.append(Metcalf.floor_study[x].capacity)
    floorpop.append(Metcalf.floor_study[x].population)

@app.route("/Metcalf")
def metcalf():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Metcalf.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Metcalf.buildingname,capacity = Metcalf.capacity, \
    population = Metcalf.population,number_floors = Metcalf.no_floor,number_studyfloors = Metcalf.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Metcalf.type,subtype = Metcalf.subtype,address = Metcalf.address)
##########################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Photonics.no_floors_study):
    floornumber.append(Photonics.floor_study[x].level)
    floorcap.append(Photonics.floor_study[x].capacity)
    floorpop.append(Photonics.floor_study[x].population)

@app.route("/Photonics")
def photonics():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Photonics.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Photonics.buildingname,capacity = Photonics.capacity, \
    population = Photonics.population,number_floors = Photonics.no_floor,number_studyfloors = Photonics.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Photonics.type,subtype = Photonics.subtype,address = Photonics.address)
##############################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Wheelock.no_floors_study):
    floornumber.append(Wheelock.floor_study[x].level)
    floorcap.append(Wheelock.floor_study[x].capacity)
    floorpop.append(Wheelock.floor_study[x].population)

@app.route("/Wheelock")
def wheelock():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Wheelock.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Wheelock.buildingname,capacity = Wheelock.capacity, \
    population = Wheelock.population,number_floors = Wheelock.no_floor,number_studyfloors = Wheelock.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Wheelock.type,subtype = Wheelock.subtype,address = Wheelock.address)
##################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Yawkey.no_floors_study):
    floornumber.append(Yawkey.floor_study[x].level)
    floorcap.append(Yawkey.floor_study[x].capacity)
    floorpop.append(Yawkey.floor_study[x].population)

@app.route("/Yawkey")
def yawkey():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Yawkey.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Yawkey.buildingname,capacity = Yawkey.capacity, \
    population = Yawkey.population,number_floors = Yawkey.no_floor,number_studyfloors = Yawkey.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Yawkey.type,subtype = Yawkey.subtype,address = Yawkey.address)
#################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Howard_Therman_Center.no_floors_study):
    floornumber.append(Howard_Therman_Center.floor_study[x].level)
    floorcap.append(Howard_Therman_Center.floor_study[x].capacity)
    floorpop.append(Howard_Therman_Center.floor_study[x].population)

@app.route("/Howard_Therman_Center")
def htc():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Howard_Therman_Center.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Howard_Therman_Center.buildingname,capacity = Howard_Therman_Center.capacity, \
    population = Howard_Therman_Center.population,number_floors = Howard_Therman_Center.no_floor,number_studyfloors = Howard_Therman_Center.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Howard_Therman_Center.type,subtype = Howard_Therman_Center.subtype,address = Howard_Therman_Center.address)
#####################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Cas.no_floors_study):
    floornumber.append(Cas.floor_study[x].level)
    floorcap.append(Cas.floor_study[x].capacity)
    floorpop.append(Cas.floor_study[x].population)

@app.route("/Cas")
def cas():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Cas.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Cas.buildingname,capacity = Cas.capacity, \
    population = Cas.population,number_floors = Cas.no_floor,number_studyfloors = Cas.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Cas.type,subtype = Cas.subtype,address = Cas.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Cfa.no_floors_study):
    floornumber.append(Cfa.floor_study[x].level)
    floorcap.append(Cfa.floor_study[x].capacity)
    floorpop.append(Cfa.floor_study[x].population)

@app.route("/Cfa")
def cfa():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'cfa.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Cfa.buildingname,capacity = Cfa.capacity, \
    population = Cfa.population,number_floors = Cfa.no_floor,number_studyfloors = Cfa.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Cfa.type,subtype = Cfa.subtype,address = Cfa.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Cgs.no_floors_study):
    floornumber.append(Cgs.floor_study[x].level)
    floorcap.append(Cgs.floor_study[x].capacity)
    floorpop.append(Cgs.floor_study[x].population)

@app.route("/Cgs")
def cgs():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'cgs.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Cgs.buildingname,capacity = Cgs.capacity, \
    population = Cgs.population,number_floors = Cgs.no_floor,number_studyfloors = Cgs.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Cgs.type,subtype = Cgs.subtype,address = Cgs.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Com.no_floors_study):
    floornumber.append(Com.floor_study[x].level)
    floorcap.append(Com.floor_study[x].capacity)
    floorpop.append(Com.floor_study[x].population)

@app.route("/Com")
def com():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'com.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Com.buildingname,capacity = Com.capacity, \
    population = Com.population,number_floors = Com.no_floor,number_studyfloors = Com.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Com.type,subtype = Com.subtype,address = Com.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Epic.no_floors_study):
    floornumber.append(Epic.floor_study[x].level)
    floorcap.append(Epic.floor_study[x].capacity)
    floorpop.append(Epic.floor_study[x].population)

@app.route("/Epic")
def epic():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'epic.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Epic.buildingname,capacity = Epic.capacity, \
    population = Epic.population,number_floors = Epic.no_floor,number_studyfloors = Epic.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Epic.type,subtype = Epic.subtype,address = Epic.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Rich.no_floors_study):
    floornumber.append(Rich.floor_study[x].level)
    floorcap.append(Rich.floor_study[x].capacity)
    floorpop.append(Rich.floor_study[x].population)

@app.route("/Rich")
def rich():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'RichHall.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Rich.buildingname,capacity = Rich.capacity, \
    population = Rich.population,number_floors = Rich.no_floor,number_studyfloors = Rich.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Rich.type,subtype = Rich.subtype,address = Rich.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Sleeper.no_floors_study):
    floornumber.append(Sleeper.floor_study[x].level)
    floorcap.append(Sleeper.floor_study[x].capacity)
    floorpop.append(Sleeper.floor_study[x].population)

@app.route("/Sleeper")
def sleeper():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Sleeper.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Sleeper.buildingname,capacity = Sleeper.capacity, \
    population = Sleeper.population,number_floors = Sleeper.no_floor,number_studyfloors = Sleeper.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Sleeper.type,subtype = Sleeper.subtype,address = Sleeper.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Claflin.no_floors_study):
    floornumber.append(Claflin.floor_study[x].level)
    floorcap.append(Claflin.floor_study[x].capacity)
    floorpop.append(Claflin.floor_study[x].population)

@app.route("/Claflin")
def claflin():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Claflin.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Claflin.buildingname,capacity = Claflin.capacity, \
    population = Claflin.population,number_floors = Claflin.no_floor,number_studyfloors = Claflin.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Claflin.type,subtype = Claflin.subtype,address = Claflin.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,TenNineteen.no_floors_study):
    floornumber.append(TenNineteen.floor_study[x].level)
    floorcap.append(TenNineteen.floor_study[x].capacity)
    floorpop.append(TenNineteen.floor_study[x].population)

@app.route("/TenNineteen")
def tennineteen():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'TenNineteen.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = TenNineteen.buildingname,capacity = TenNineteen.capacity, \
    population = TenNineteen.population,number_floors = TenNineteen.no_floor,number_studyfloors = TenNineteen.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = TenNineteen.type,subtype = TenNineteen.subtype,address = TenNineteen.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Warren.no_floors_study):
    floornumber.append(Warren.floor_study[x].level)
    floorcap.append(Warren.floor_study[x].capacity)
    floorpop.append(Warren.floor_study[x].population)

@app.route("/Warren")
def warren():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Warrentowers.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Warren.buildingname,capacity = Warren.capacity, \
    population = Warren.population,number_floors = Warren.no_floor,number_studyfloors = Warren.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Warren.type,subtype = Warren.subtype,address = Warren.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Towers.no_floors_study):
    floornumber.append(Towers.floor_study[x].level)
    floorcap.append(Towers.floor_study[x].capacity)
    floorpop.append(Towers.floor_study[x].population)

@app.route("/Towers")
def towers():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Towers.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Towers.buildingname,capacity = Towers.capacity, \
    population = Towers.population,number_floors = Towers.no_floor,number_studyfloors = Towers.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Towers.type,subtype = Towers.subtype,address = Towers.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Myles.no_floors_study):
    floornumber.append(Myles.floor_study[x].level)
    floorcap.append(Myles.floor_study[x].capacity)
    floorpop.append(Myles.floor_study[x].population)

@app.route("/Myles")
def myles():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'MylesStandishHall.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Myles.buildingname,capacity = Myles.capacity, \
    population = Myles.population,number_floors = Myles.no_floor,number_studyfloors = Myles.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Myles.type,subtype = Myles.subtype,address = Myles.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Kilachand.no_floors_study):
    floornumber.append(Kilachand.floor_study[x].level)
    floorcap.append(Kilachand.floor_study[x].capacity)
    floorpop.append(Kilachand.floor_study[x].population)

@app.route("/Kilachand")
def kilachand():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Kilachand_Hall.jpeg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Kilachand.buildingname,capacity = Kilachand.capacity, \
    population = Kilachand.population,number_floors = Kilachand.no_floor,number_studyfloors = Kilachand.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Kilachand.type,subtype = Kilachand.subtype,address = Kilachand.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Danielsen.no_floors_study):
    floornumber.append(Danielsen.floor_study[x].level)
    floorcap.append(Danielsen.floor_study[x].capacity)
    floorpop.append(Danielsen.floor_study[x].population)

@app.route("/Danielsen")
def danielsen():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'DanielsenHall.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Danielsen.buildingname,capacity = Danielsen.capacity, \
    population = Danielsen.population,number_floors = Danielsen.no_floor,number_studyfloors = Danielsen.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Danielsen.type,subtype = Danielsen.subtype,address = Danielsen.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Mugar.no_floors_study):
    floornumber.append(Mugar.floor_study[x].level)
    floorcap.append(Mugar.floor_study[x].capacity)
    floorpop.append(Mugar.floor_study[x].population)

@app.route("/Mugar")
def mugar():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Mugar.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Mugar.buildingname,capacity = Mugar.capacity, \
    population = Mugar.population,number_floors = Mugar.no_floor,number_studyfloors = Mugar.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Mugar.type,subtype = Mugar.subtype,address = Mugar.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Lse.no_floors_study):
    floornumber.append(Lse.floor_study[x].level)
    floorcap.append(Lse.floor_study[x].capacity)
    floorpop.append(Lse.floor_study[x].population)

@app.route("/Lse")
def lse():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Lse.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Lse.buildingname,capacity = Lse.capacity, \
    population = Lse.population,number_floors = Lse.no_floor,number_studyfloors = Lse.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Lse.type,subtype = Lse.subtype,address = Lse.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Questrom.no_floors_study):
    floornumber.append(Questrom.floor_study[x].level)
    floorcap.append(Questrom.floor_study[x].capacity)
    floorpop.append(Questrom.floor_study[x].population)

@app.route("/Questrom")
def questrom():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Questrom.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Questrom.buildingname,capacity = Questrom.capacity, \
    population = Questrom.population,number_floors = Questrom.no_floor,number_studyfloors = Questrom.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Questrom.type,subtype = Questrom.subtype,address = Questrom.address)
############################################################################################################################################
floornumber.clear()
floorcap.clear()
floorpop.clear()
for x in range(0,Law.no_floors_study):
    floornumber.append(Law.floor_study[x].level)
    floorcap.append(Law.floor_study[x].capacity)
    floorpop.append(Law.floor_study[x].population)

@app.route("/Law")
def law():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'Law.jpg')
    return render_template("Building.html",image =pic1,image2=pic2,Page = Law.buildingname,capacity = Law.capacity, \
    population = Law.population,number_floors = Law.no_floor,number_studyfloors = Law.no_floors_study,current_floor = floornumber,current_pop=floorpop,current_cap=floorcap,BuildingType = Law.type,subtype = Law.subtype,address = Law.address)
