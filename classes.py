
class Floor:

    def __init__(self):
        self.population = 3        
        self.capacity = 4


class Building:
    
    def __init__(self,floors):
        
        self.capacity = 100 
        self.no_floor = 0
        self.floor_study = floors
        self.no_floors_study = len(floors)
        self.population = 0
        self.type = "a"
        self.buildingname = "building"
        self.subtype = "b"
        self.address = "141 nonexistent st."
#Building class Must pass (int capacty, int.no_floor, int floor_study, string building name, string building type, string subtype, string address)
 

 