"""
Exercise 4
GE 120: Introduction to Object Oriented Programming
"""

from math import cos, sin, radians, sqrt

class Line: #This helps us encapsulates the data and functionalities related to distance and azimuth. 
    def __init__(self, distance, azimuth): 
        self.distance = distance # Initialize distance attribute
        self.azimuth = azimuth # Initialize azimuth attribute
    
    def latitude (self):
        '''
        Compute for the lat of a given line

        Input:
        distance - float
        azimuth - float

        Output:
        latitude - float
        '''
        latitude = float(self.distance)*cos(radians(self.azimuth))
        return latitude
    
    def departure (self): 
        '''
        Compute for the departure of a given line.
        Input:
        distance - float
        azimuth - float

        Ouput:
        departure - float
        '''

        departure = float(self.distance) * sin (radians(self.azimuth))

        return departure
    
    def bearing (self): 
        '''
        Compute for the DMS bearing of a given angle.

        Input
        azimuth - float

        Output:
        bearing - string

        '''

        # Compute bearing based on the azimuth
        if azimuth > 0 and azimuth < 90:
            bearing = 'S {:^5} W'.format (round(azimuth,3))
        elif azimuth > 90 and azimuth < 180:
            bearing = 'N {:^5} W' .format (round(180-azimuth,3))
        elif azimuth > 180 and azimuth < 270:
            bearing = 'N {: ^5} E' .format (round(azimuth-180,3))
        elif azimuth > 270 and azimuth < 360:
            bearing = 'S {:^5} E' .format (round(360-azimuth,3))
        else:
            bearing = "INVALID"
        
        return bearing

class Cardinal(Line):

    def __init__(self,distance,azimuth):
        super().__init__(distance,azimuth) # Call parent class initializer


    def bearing (self):
        """
        Compute the bearing for cardinal directions.

        Output:
        bearing - string
        """
        if azimuth == 0:
            bearing = "DUE SOUTH"
        elif azimuth == 90:
            bearing = "DUE WEST"
        elif azimuth == 270:
            bearing = "DUE EAST"
        else:
            bearing = "INVALID"
        return bearing

#The next lines will initialize our attributes

counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

while True:
    print ()
    print("Line {}-{}".format(counter, counter + 1))

    invalid_input = False
    while not (invalid_input):
        distance = input ("Distance: ")
        if invalid_input:
            print ("INVALID INPUT")
            continue
        if not (invalid_input):
            break
    azimuth = input ("Azimuth from the South: ")
    if "-" in str(azimuth):
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int (minutes)/60) + (float (seconds)/3600))% 360
    else:
        azimuth = float (azimuth) % 360
    if azimuth % 90 ==0:
        line = Cardinal (distance, azimuth) # Creates Cardinal object if azimuth is a multiple of 90
    else: 
        line = Line(distance, azimuth) # Otherwise, it creates Line object
    
    #The next lines accumulate for the summation of lat, dep, and distance.
    sumLat += line.latitude()
    sumDep += line.departure()
    sumDist += float(line.distance)

    lines.append ((counter, line.distance, line.bearing (), line.latitude (), line.departure ()))

    yn = input ("Add new line? ")
    if yn.lower () == "yes" or yn.lower () == "y":
        counter = counter+1
        continue
    else: 
        break

# The next lines will help us present our data in table. 

print ("\n\n")
print ('{: ^10} {: ^10} {: ^10} {: ^12} {: ^10}'.format ("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
for line in lines:
    print ('{: ^10} {: ^10} {: ^10} {: ^12} {: ^10}'.format (line[0], line [1], line [2], round(line [3],3), round (line [4],3)))

# For the final part, we print the sums of our latitude, departure, and distance. We can use these values to calculate our LEC and REC.

print ()
print ("SUMMATION OF LAT: ", round (sumLat,3))
print ()
print ("SUMMATION OF DEP: ", round (sumDep, 3))
print ()
print ("TOTAL DISTANCE: ", round (sumDist,3))

LEC = sqrt((sumLat)**2 + (sumDep)**2) #Compute LEC
print("LEC = ", round (LEC,3))
print ()
rec = sumDist / LEC  #Compute REC
print("REC = 1: {:.2f}".format(round(rec,-3)))


print ("- - - - - - - - - - - - 🎀 𝓔𝓝𝓓 🎀 - - - - - - - - - - -  ")