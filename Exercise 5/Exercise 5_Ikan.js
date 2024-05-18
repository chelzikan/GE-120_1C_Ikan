/*
Exercise 5
Coding with JavaScript

Chelzy L. Ikan
2023-03942
*/


function getLatitude(distance, azimuth) {
    /*
    this function will help us calculate the latitude of our lines.

    input - float type of azimuth and distance
    output - float type latitude

    */

    if (azimuth % 180 ==90) {
        return 0;
    } else {
        return -distance * Math.cos(azimuth * Math.PI / 180.0);
    }
}

function getDeparture(distance, azimuth) {
     /*
    this function will help us calculate the departure of our lines.

    input - float type of azimuth and distance
    output - float type departure

    */
    if (azimuth % 0 == 360) {
        return 0;
    } else {
        return -distance * Math.sin(azimuth * Math.PI / 180.0);
    }
}

function azimuthToBearing(azimuth) {
     /*
    this function will help us calculate the bearing of our lines (in degrees form only)

    input - float type of azimuth (in degrees)
    output - float type bearing

    */
    if (azimuth > 0 && azimuth < 90) {
        return `S ${azimuth} W`;
    } else if (azimuth > 90 && azimuth < 180) {
        return `N ${180 - azimuth} W`;
    } else if (azimuth > 180 && azimuth < 270) {
        return `N ${(azimuth - 180).toPrecision(5)} E`;
    } else if (azimuth > 270 && azimuth < 360) {
        return `N ${360 - azimuth} E`;
    } else if (azimuth == 0 || azimuth == 360) {
        return 'DUE SOUTH';
    } else if (azimuth == 90) {
        return 'DUE WEST';
    } else if (azimuth == 180) {
        return 'DUE NORTH';
    } else if (azimuth == 270) {
        return 'DUE EAST';
    } else {
        return 'INVALID';
    }
}

// For the following section, we will iterate through our data to calculate the details (lat, dep, and bearing) of our line.

let data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562]
];

let lines = [];

let sumLat = 0;
let sumDep = 0;
let sumDist = 0;

for (let i = 0; i < data.length; i++) {
    let line = data[i];
    let distance = line[0];
    let azimuth = line[1];

    let bearing = azimuthToBearing(azimuth);
    let lat = getLatitude(distance, azimuth);
    let dep = getDeparture(distance, azimuth);

//  ↓ Accumulate the sums of latitude, departure, and distance
    sumLat += lat;
    sumDep += dep;
    sumDist += distance;

    lines.push([i + 1, distance, bearing, lat, dep]); // This line will store line details in lines array
}

// Presenting our calculated values into table ↓ 
console.log("Line No.".padEnd(10), "Distance".padEnd(10), "Bearing".padEnd(16), "Latitude".padEnd(15), "Departure".padEnd(15));
for (let line of lines) {
    console.log(
        line[0].toString().padEnd(10), //We use toString to properly align our columns, since padEnd operates only with strings.
        line[1].toString().padEnd(10),
        line[2].padEnd(16),
        line[3].toPrecision(5).toString().padEnd(15),
        line[4].toPrecision(5).toString().padEnd(15)
    );
}

// 
console.log ();
console.log("Σ of Latitude = ", sumLat.toPrecision(5));

console.log("Σ of Departure = ", sumDep.toPrecision(5));

console.log("Σ of Distance = ", sumDist.toPrecision(5));


// ↓ Calculating the LEC and REC:

let LEC = Math.sqrt(sumLat ** 2 + sumDep ** 2);
console.log("LEC = ", LEC.toPrecision(5));
console.log();

let rec = sumDist / LEC;
console.log("REC = 1:", Math.round(rec / 1000) * 1000);


console.log ();
console.log("- - - - - - - - - - - - - - - - END - - - - - - - - - - - - - - - -");



