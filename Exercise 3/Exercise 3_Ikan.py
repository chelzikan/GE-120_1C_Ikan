"""

Exercise 3

"""

from math import cos, sin, radians, sqrt #To begin our exercise 3, we first import necesarry math functions. 

def getLatitude(distance, azimuth):
    '''
    This function will help us compute for the latitude of a line.

    Input:
    distance - float
    azimuth - float

    Output:
    latitude - float

    '''
    latitude = -distance * cos(radians(float(azimuth)))
    return latitude

def getDeparture(distance, azimuth):
    '''
    This function will help us compute for the departure of a line.

    Input:
    distance - float
    azimuth - float

    Output:
    departure - float
    '''
    departure = -distance * sin(radians(float(azimuth)))
    return departure

def azimuthToBearing(azimuth):
    '''
    This function will help us calculate for our DMS bearing.

    Input:
    azimuth - float

    Output:
    bearing - string

    '''

    if "-" in azimuth: # If the azimuth was entered as DMS instead of decimal, we use this conversion. 
        degrees, minutes, seconds = map(int, azimuth.split("-"))
        azimuth_decimal = degrees + (minutes / 60) + (seconds / 3600)
    else:
        azimuth_decimal = float(azimuth) % 360

    degrees_int = int(azimuth_decimal)
    minutes_float = (azimuth_decimal - degrees_int) * 60
    minutes_int = int(minutes_float)
    seconds_float = (minutes_float - minutes_int) * 60

# The next lines will help us convert our Azimuths to Bearings. 
    if azimuth_decimal > 0 and azimuth_decimal < 90:
        bearing = 'S {: >2}° {: >2}\' {:.2f}" W'.format(degrees_int, minutes_int, seconds_float)
    elif azimuth_decimal > 90 and azimuth_decimal < 180:
        bearing = 'N {: >2}° {: >2}\' {:.2f}" W'.format(int(180 - azimuth_decimal), int(((180 - azimuth_decimal) % 1) * 60), int((((180 - azimuth_decimal) % 1) * 60) % 1 * 60))
    elif azimuth_decimal > 180 and azimuth_decimal < 270:
        bearing = 'N {: >2}° {: >2}\' {:.2f}" E'.format(int(azimuth_decimal - 180), int(((azimuth_decimal - 180) % 1) * 60), int((((azimuth_decimal - 180) % 1) * 60) % 1 * 60))
    elif azimuth_decimal > 270 and azimuth_decimal < 360:
        bearing = 'S {: >2}° {: >2}\' {:.2f}" E'.format(int(360 - azimuth_decimal), int(((360 - azimuth_decimal) % 1) * 60), int((((360 - azimuth_decimal) % 1) * 60) % 1 * 60))
    elif azimuth_decimal == 0:
        bearing = "DUE SOUTH"
    elif azimuth_decimal == 360:
        bearing = "DUE SOUTH"
    elif azimuth_decimal == 90:
        bearing = "DUE WEST"
    elif azimuth_decimal == 180:
        bearing = "DUE NORTH"
    elif azimuth_decimal == 270:
        bearing = "DUE EAST"
    else:
        bearing = "INVALID"

    return bearing

# Create a sentinel controlled loop
counter = 1
lines = []

sumLat = 0
sumDep = 0
sumDist = 0

while True:
    print()
    print("Line {}-{}".format(counter, counter + 1)) 

    distance = input("Distance: ")
    azimuth = input("Azimuth from the South: ")

    bearing = azimuthToBearing(azimuth)
    lat = getLatitude(float(distance), float(azimuth))
    dep = getDeparture(float(distance), float(azimuth))

    sumLat += lat
    sumDep += dep
    sumDist += float(distance)

    line = ('{}-{}'.format(counter, counter + 1), distance, bearing, lat, dep)
    lines.append(line)

    # Ask for input
    yn = input("Add new line? (y/n) ")
    if yn and (yn.lower() == "yes" or yn.lower() == "y"): 
        counter += 1
        continue
    else:
        break

# Then, we present the gathered data in a table.

print("\n\n")
print('{: ^10} {: ^10} {: ^20} {: ^22} {: ^16}'.format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))

for line in lines:
    print('{: ^10} {: ^10} {: ^20} {: ^20.2f} {: ^20f}'.format(line[0], line[1], line[2], line[3], line[4])) 

print ()

# Next, we calculate the sums of our latitude, departure, and distance. We can use these values to calculate our LEC and REC.

print("Σ OF LATITUDE  = ", sumLat)
print ()
print("Σ OF DEPARTURE = ", sumDep)
print ()
print("Σ OF DISTANCE  = ", sumDist)
print ()

LEC = sqrt((sumLat)**2 + (sumDep)**2)
print("LEC = ", LEC)
print ()
rec = sumDist / LEC  
print("REC = 1: {:.2f}".format(rec))

# For this final section, we will use the total sums to adjust the latitude and departure for every line.

constCorrLat = sumLat / sumDist
constCorrDep = sumDep / sumDist

for i, line in enumerate(lines):
    corr_lat = constCorrLat * float(line[1])
    corr_dep = constCorrDep * float(line[1])

    adjLat = line[3] + corr_lat
    adjDep = line[4] + corr_dep

    lines[i] = (line[0], line[1], line[2], adjLat, adjDep)

print(" ---------------------------------END--------------------------------- ")