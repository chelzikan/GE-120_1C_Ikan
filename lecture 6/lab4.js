/*
GE 120: Intro to OOP for Geomatic Application
Chelzy L. Ikan
2023-03942
*/

function getLatitude(distance, azimuth){
    /*
    This function will help us compute for the latitude of a line.

    Input:
    distance - float
    azimuth - float

    Output:
    latitude - float

    */
    var latitude = -distance * cos(Math.radians(azimuth))
    return latitude
}
function getDeparture(distance, azimuth){
    /*
    This function will help us compute for the departure of a line.

    Input:
    distance - float
    azimuth - float

    Output:
    departure - float
    */
    departure = -distance * sin(Math.radians(azimuth))
    return departure
}
function azimuthToBearing(azimuth){
    /*
    This function will help us calculate for our DMS bearing.

    Input:
    azimuth - float

    Output:
    bearing - string

    */

    
        azimuth_decimal = (azimuth) % 360

}
// The next lines will help us convert our Azimuths to Bearings. 
    if (azimuth_decimal) > 0 and azimuth_decimal < 90 {
        bearing = 'S {: >2}° {: >2}\' {:.2f}" W'.format(degrees_int, minutes_int, seconds_float)}
    elif azimuth_decimal > 90 and azimuth_decimal < 180{
        bearing = 'N {: >2}° {: >2}\' {:.2f}" W'.format(int(180 - azimuth_decimal), int(((180 - azimuth_decimal) % 1) * 60), int((((180 - azimuth_decimal) % 1) * 60) % 1 * 60))}
        elif azimuth_decimal > 180 and azimuth_decimal < 270{
        bearing = 'N {: >2}° {: >2}\' {:.2f}" E'.format(int(azimuth_decimal - 180), int(((azimuth_decimal - 180) % 1) * 60), int((((azimuth_decimal - 180) % 1) * 60) % 1 * 60))}
        elif azimuth_decimal > 270 and azimuth_decimal < 360{
        bearing = 'S {: >2}° {: >2}\' {:.2f}" E'.format(int(360 - azimuth_decimal), int(((360 - azimuth_decimal) % 1) * 60), int((((360 - azimuth_decimal) % 1) * 60) % 1 * 60))}
    elif azimuth_decimal == 0{
        bearing = "DUE SOUTH"}
    elif azimuth_decimal == 360:
        bearing = "DUE SOUTH"
    elif azimuth_decimal == 90:
        bearing = "DUE WEST"
    elif azimuth_decimal == 180:
        bearing = "DUE NORTH"
    elif azimuth_decimal == 270{}
        bearing = "DUE EAST"
    else {
        bearing = "INVALID"

    return bearing
    }
//  Create a sentinel controlled loop
counter = 1
var lines = []

[13.23 , 124.795],
[15.57 , 014.143],
[43.36 , 270.000],
[23.09 , 188.169],
[10.99 , 180.000],
[41.40 , 050.562]

sumLat = 0
sumDep = 0
sumDist = 0

for {var = 0; i < }

while (true) {
    console.log()
    console.log("Line {}-{}".format(counter, counter + 1)) 


    let bearing = azimuthToBearing(azimuth)
    let lat = getLatitude(float(distance), float(azimuth))
    let dep = getDeparture(float(distance), float(azimuth))

    sumLat += lat
    sumDep += dep
    sumDist += float(distance)

    line = ['{}-{}'.format(counter, counter + 1), distance, bearing, lat, dep]
    lines.push(line)

}
// # Then, we present the gathered data in a table.

console.log("\n\n")
console.log('{: ^10} {: ^10} {: ^20} {: ^22} {: ^16}'.format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))

for line in lines:
    console.log('{: ^10} {: ^10} {: ^20} {: ^20.2f} {: ^20f}'.format(line[0], line[1], line[2], line[3], line[4])) 

console.log ()

// # Next, we calculate the sums of our latitude, departure, and distance. We can use these values to calculate our LEC and REC.

console.log("Σ OF LATITUDE  = ", sumLat)
console.log ()
console.log("Σ OF DEPARTURE = ", sumDep)
console.log ()
console.log("Σ OF DISTANCE  = ", sumDist)
console.log ()

LEC = sqrt((sumLat)**2 + (sumDep)**2)
console.log("LEC = ", LEC)
console.log ()
rec = sumDist / LEC  
console.log("REC = 1: {:.2f}".format(rec))

// # For this final section, we will use the total sums to adjust the latitude and departure for every line.

constCorrLat = sumLat / sumDist
constCorrDep = sumDep / sumDist

for i, line in enumerate(lines):
    corr_lat = constCorrLat * float(line[1])
    corr_dep = constCorrDep * float(line[1])

    adjLat = line[3] + corr_lat
    adjDep = line[4] + corr_dep

    lines[i] = (line[0], line[1], line[2], adjLat, adjDep)

console.log(" ---------------------------------END--------------------------------- ")