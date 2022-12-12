
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
        for i in range(len(floors)):

            self.capacity += self.floor_study[i].capacity
            self.population += self.floor_study[i].population
         
        
        self.type = buildingtype
        self.buildingname = name
        self.subtype = subtype
        self.address = address
        self.x = x
        self.y = y
    


 
