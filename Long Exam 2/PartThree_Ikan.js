/*
App Title - AzimuthtoBearingConverter

React native components to be used:

View - This will contain the text input, text, and button. I plan to have an outer box that will contain 2 inner boxes. for the 
first box (box1), it will have 2 more inner boxes: box1a where u can input values, and box 1b which contains the button. for the second box (box 2), it will contain the output. 
Text - The texts I want to disply are "Welcome to Azimuth to Bearing Converter.",  and the converted values itself.
TextInput - This is the element where the DMS value can be inputted. I will input a note above the input box stating that this only accepts and returns Azimuth from the South DMS values
Button - Once the button is clicked, it will display a text located in box 2.

*/

let azimuthInput = prompt("Azimuth in DMS: ");
let [deg, min, sec] = azimuthInput.split(" ").map(Number);

function DMStoDD(deg, min, sec) { //We need to convert our DMS first to DD so it'll be easy for us to calculat its bearing
    return deg + (min / 60) + (sec / 3600);
}

function convertToBearing(azimuth) { //this function will help us convert our azimuth to bearing
    if (azimuth > 0 && azimuth < 90) {
        return `S ${DDtoDMS(azimuth)} W`;
    } else if (azimuth > 90 && azimuth < 180) {
        return `N ${DDtoDMS(180 - azimuth)} W`;
    } else if (azimuth > 180 && azimuth < 270) {
        return `N ${DDtoDMS(azimuth - 180)} E`;
    } else if (azimuth > 270 && azimuth < 360) {
        return `S ${DDtoDMS(360 - azimuth)} E`;
    } else if (azimuth === 0 || azimuth === 360) {
        return 'DUE SOUTH';
    } else if (azimuth === 90) {
        return 'DUE WEST';
    } else if (azimuth === 180) {
        return 'DUE NORTH';
    } else if (azimuth === 270) {
        return 'DUE EAST';
    } else {
        return 'INVALID';
    }
}

function DDtoDMS(decimalDegrees) { //now that we already have our bearing in decimal, we need to transform it back to DD.
    let deg = Math.floor(decimalDegrees);
    let minFloat = (decimalDegrees - deg) * 60;
    let min = Math.floor(minFloat);
    let sec = (minFloat - min) * 60;
    return `${deg} ${min} ${sec.toPresion(4)}`;
}

let azimuthDecimal = DMStoDD(deg, min, sec);
let bearing = convertToBearing(azimuthDecimal);

console.log("Bearing in DMS is:", bearing);
