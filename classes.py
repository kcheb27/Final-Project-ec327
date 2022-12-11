
class Floor:

    def __init__(self,pop,cap,floor_no):
        self.population = pop      
        self.capacity = cap
        self.level = floor_no


class Building:
    
    def __init__(self,floors,amount_floors,buildingtype,subtype,name,address,x,y):

        
        self.no_floor = amount_floors
        self.floor_study = floors
        self.no_floors_study = len(floors)
        self.capacity = 0
        self.population = 0
        for x in floors:
            self.capacity = self.capacity + x.capacity
            self.population = self.population + x.population

        self.type = buildingtype
        self.buildingname = name
        self.subtype = subtype
        self.address = address
        self.x_loc = x
        self.y_loc = y
        self.distance = 0
 




 
