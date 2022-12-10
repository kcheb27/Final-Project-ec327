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




app = Flask(__name__)





print("hello")

@app.route('/upload',methods=["GET", "POST"])
def hello():
    return '<h1>Hello, cheese!</h1>'
