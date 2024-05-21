class Parcel: # #This will help us encapsulates the data and functionalities related to attributes owner and area. 
    def __init__ (self, owner, area):
        self.owner = str (owner)
        self.area = int (area)

    def name (self):
        return f"{self.owner}"
    
    def areaOfLand (self):
        return f"{self.area}"

    def getClassification (self):
        '''
        Classifies the parcel of land
        
        '''
        areaInHectares = self.area/10, 000
        if areaInHectares < 1:
            getClassification = "Residential"
        elif areaInHectares>1 and self.area<12:
            getClassification = "Private Agricultural"
        elif areaInHectares> 12:
            getClassification = "Public Agricultural"
        else:
            getClassification = "Cannot be classified"
        
        return getClassification
    def output (self):
        return f"A parcel of land owned by {self.owner} with an area of {self.area} square meters"


class Riparian(Parcel): #Riparian is the child class, while Parcel is the parent class.

    def __init__(self,owner,area):
        super().__init__(owner,area) # This calls the parent class initializer
        self.type = type
        return f"A parcel of land owned by {self.owner}, with an area of {self.area}"
    def getAdjoiningWaterbody (self):
        if self.type ==1:
            return "Adjacent to River - can be subject to tilting"
        elif self.type ==2:
            return "Adjacent to Ocean (Littoral) - cannot be subject to titling"
        else:
            return "Invalid Riparian Parcel"

    
owner = input ("Owner: ")
area = input ("Area in squaremeters")
other_owner = Parcel (str (input ("name: ")), int ((input ("area: "))))


print (("Consolidated lot of ", other_owner.name () "and " , {self.owner} "with a total area of ", int (other_owner.areaOfland ()) + {self.area} "square meters"))






