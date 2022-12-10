from flask import Flask
from classes import Floor
from classes import Building


#example Building make: StuVi 1
floor_list1 = [Floor(10,20,1),Floor(10,30,2)]
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
CAS = Building(floor_list14, 5, "School", "N/a", "CAS", "725 Commonwealth Ave")
floor_list15 = [Floor(45,80,1),Floor(22,40,2), Floor(18,30,3)]
CFA = Building(floor_list15,5,"School","N/a","CFA", "855 Commonwealth Ave")
floor_list16 = [Floor(22,40,1),Floor(18,30,2), Floor(11,20,3)]
CGS = Building(floor_list16,4, "School","N/a","CGS","871 Commonwealth Ave")
floor_list17 = [Floor(18,30,1),Floor(22,40,2)]
COM = Building(floor_list17, 3, "School","N/a","COM","640 Commonwealth Ave")
floor_list18 = [Floor(6,10,1),Floor(65,100,2)]
EPIC = Building(floor_list18, 2, "School", "N/a", "EPIC", "750 Commonwealth Ave")


app = Flask(__name__)





print("hello")

@app.route('/upload',methods=["GET", "POST"])
def hello():
    return '<h1>Hello, cheese!</h1>'
