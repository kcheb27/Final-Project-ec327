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

floor_list_stuvi2 = [Floor(10,20,1),Floor(10,30,2),Floor(30,80,26)]
StuVi1 = Building(floor_list_stuvi2,26,"Dorm","N/a","StuVi2","33 Harry Agganis Way")

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

app = Flask(__name__)
picFolder = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    return render_template("index.html",name ="Tim",image =pic1,Page = "Home Page")
@app.route("/GSU")
def gsu():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'bulogo.png')
    return render_template("GSU.html",image =pic1,Page = Gsu.buildingname,capacity = Gsu.capacity)