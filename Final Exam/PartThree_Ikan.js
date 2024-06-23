/*
Chelzy L. Ikan
2023-03942
*/

//Part A
function parseBearing(bearing) {
    /*
    Converts bearing in string format to azimuth from the South.
    */
    let direction1 = bearing.charAt(0); // Extracts the first direction of the bearing (either N or S only) 
    let direction2 = bearing.slice(-1); // Extracts the second direction of the bearing (either E or W only) 
    let degreesMinutes = bearing.slice(1, -1); // Extracts the degrees & minutes part of the bearing

    // Splitting the degrees and minutes
    let value = degreesMinutes.split("d");
    let degrees = parseInt(value[0]); 
    let minutes = parseFloat(value[1]);

    let decimalDegrees = degrees + minutes / 60; //Convert DM to DD

    // Computing Azimuth from the South
    let azimuth;
    if (direction1 === "N" && direction2 === "E") {
        azimuth = 180 + decimalDegrees;
    } else if (direction1 === "N" && direction2 === "W") {
        azimuth = 180 - decimalDegrees;
    } else if (direction1 === "S" && direction2 === "E") {
        azimuth = 270 + decimalDegrees;
    } else if (direction1 === "S" && direction2 === "W") {
        azimuth = decimalDegrees;
    }

    azimuth = (azimuth + 360) % 360; 
    return azimuth;
}

// Example: 
console.log((parseBearing("S45d30W")).toPrecision(5));
console.log((parseBearing("N23d52E")).toPrecision(5)); 


// PART B
function convertAzimuthToRadians (azimuthInDegrees){
    /*
    Converts the azimuth from degrees to radians
    input - azimuth in degrees
    output - azimuth in radians
    */
    azimuthInRadians = azimuthInDegrees * (Math.PI / 180)
    return azimuthInRadians
}

function computeLatitude(distance, azimuthInRadians) {
    /*
    Calculates the latitude of our lines.

    input - azimuth in radians and distance
    output - float type latitude

    */

    if (azimuthInRadians % 180 == 90) {
        return 0;
    } else {
        return -distance * Math.cos(azimuthInRadians);
    }
}

function computeDeparture(distance, azimuthInRadians) {
     /*
    this function will help us calculate the departure of our lines.

    input - azimuth in radians and distance
    output - float type departure

    */
    if (azimuthInRadians % 0 == 360) {
        return 0;
    } else {
        return -distance * Math.sin(azimuthInRadians);
    }
}

// Part C
let courses = [
    {"bearing": "N43d23E", "distance": 123.23},
    {"bearing": "S30d15W", "distance": 200.50},
    {"bearing": "N90d0E", "distance": 150.75}
];

function computeRunningSums (courses){
    /*
    Calculates the summation of latitudes and departures of lines.
    */

    let sumLatitudes = 0;
    let sumDepartures = 0;
    let sumDistances = 0
    
    for (let course of courses) {
    let azimuthInDegrees = parseBearing(course.bearing);
    let azimuthInRadians = convertAzimuthToRadians(azimuthInDegrees);
    let latitude = computeLatitude(course.distance,azimuthInRadians);
    let departure = computeDeparture(course.distance,azimuthInRadians);
    let distance = course.distance
    
    sumLatitudes += latitude;
    sumDepartures += departure;
    sumDistances += distance;
}

return { sumLatitudes, sumDepartures, sumDistances };

}

let sums = computeRunningSums (courses);
console.log ("Sum of Latitudes:",sums.sumLatitudes.toPrecision(5));
console.log ("Sum of Departures:",sums.sumDepartures.toPrecision(5));
console.log ("Sum of Distances:",sums.sumDistances.toPrecision(5)); //extra lang po hehe

//extra 
//Getting the LEC
let LEC = Math.sqrt(sums.sumLatitudes ** 2 + sums.sumDepartures ** 2);
console.log("LEC:",LEC.toPrecision(5));

//Getting the REC
let rec = sums.sumDistances / LEC;
console.log("REC = 1:", Math.round(rec / 1000) * 1000);

console.log ();
console.log("- - - - Thank you po - - - -");
