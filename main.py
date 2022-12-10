from flask import Flask
from classes import Floor
from classes import Building


#example Building make: StuVi 1
floor_list1 = [Floor(10,20,1),Floor(10,30,2)]
StuVi1 = Building(floor_list1,26,"Dorm","N/a","StuVi1","33 Harry Agganis Way")




app = Flask(__name__)





print("hello")

@app.route('/upload',methods=["GET", "POST"])
def hello():
    return '<h1>Hello, cheese!</h1>'
