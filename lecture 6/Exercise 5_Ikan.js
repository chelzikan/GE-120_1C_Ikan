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
    if (azimuth % 180 == 90) {return 0} else {
    return (-distance * Math.cos (azimuth * Math.PI/180.0))}
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
    if (azimuth % 180 == 90) {return 0} else {
    return (-distance * Math.sin (azimuth * Math.PI/180.0))}
}

function azimuthToBearing(azimuth){  }
    /*
    This function will help us calculate for our DMS bearing.

    Input:
    azimuth - float

    Output:
    bearing - string

    */

    
// CREATE A SENTINEL CONTROLLED LOOP

var data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562]
]

sumLat = 0
sumDep = 0
sumDist = 0


for (var i = 0; i < data.length; i++){
    //console.log 9data[i])

    let line = data [i]
    let distance = line [0]
    let azimuth = line [1]

    let bearing = azimuthToBearing (azimuth)
    let lat = getLatitude (distance, azimuth)
    let dep = getDeparture (distance, azimuth)
    
    sumLat += lat
    sumDep += dep
    sumDist += distance

    lines.push([(i+1), distance, bearing, lat, dep])
}


// console.log(lines)
// console.log ("\n\n")

// # Then, we present the gathered data in a table.

console.log ("LINE NO.".padEnd(10), "DISTANCE".padEnd(10), "BEARING".padEnd(10), "LATITUDE".padEnd(10), "DEPARTURE".padEnd(10))
for (var line of lines) {
    console.log (line [0].toString ().padEnd(10), line [1].toString ().padEnd(10), line [2].padEnd(15), line [3].toPrecision(5).toString().padEnd(10), line [4].toPrecision(5).toString().padEnd(10))
}
// # Next, we calculate the sums of our latitude, departure, and distance. We can use these values to calculate our LEC and REC.

console.log("Σ OF LATITUDE  = ", sumLat.toPrecision(5))
console.log ()
console.log("Σ OF DEPARTURE = ", sumDep.toPrecision(5))
console.log ()
console.log("Σ OF DISTANCE  = ", sumDist.toPrecision(5))
console.log ()

LEC = sqrt((sumLat)**2 + (sumDep)**2)
console.log("LEC = ", LEC.toPrecision(5))
console.log ()
rec = sumDist / LEC  
console.log("REC = 1: ", Math.floor(rec/1000))


// # For this final section, we will use the total sums to adjust the latitude and departure for every line.

constCorrLat = sumLat / sumDist
constCorrDep = sumDep / sumDist

for (let i = 0; i < lines.length; i++) {
    corr_lat = constCorrLat * float(line[1])
    corr_dep = constCorrDep * float(line[1])

    adjLat = line[3] + corr_lat
    adjDep = line[4] + corr_dep

    lines[i] = (line[0], line[1], line[2], adjLat, adjDep)
}
console.log(" ---------------------------------END--------------------------------- ")