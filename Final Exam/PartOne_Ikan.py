# 1. Give an example of a task related to geomatics that is done manually and can be optimized using programming.  What would be your plan-of-attack for this solution? 
"""
Azimuth determination thru solar observation is an example of a task that is often computed manually and can be optimized using programming.
If I were to write codes for this, I would start by creating functions that could convert the inputs of horizontal circle reading,
zenith angle/altitude, and time from DMS to DD format so I could perform the average calculation easily. 
Next, I will create a class named AzimuthCalculation that will have the attributes time, zenith angle/altitude, and HCR. After that, I will create
methods that can calculate for the mean values of each attribute and adjust values as necessary. Last, I will create a subclass which will have additional parameters
like the latitude and parallax correction. It will have methods that can compute the corrected NPD and Altitude, declination, and the azimuth itself.
This is an example of what I plan to write:

class AzimuthCalculation:
    def __init__(self, time, HCR, zenith/altitude):
        self.time = time
        self.HCR = HCR
        self.zenith/altitude = zenith_altitude
    
    def dms_to_dd(self, dms):
        pass
    
    def get_mean_HCR(self):
        adjusted_HCR = [(value + 180) if value < 180 else value for value in self.HCR]
        mean_HCR = sum(adjusted_HCR) / len(adjusted_HCR)
        return mean_HCR
    
    def get_mean_zenith_altitude(self):
        adjusted_zenith = [(360 - value) if value > 300 else value for value in self.zenith_altitude]  ** not very sure po if kapag > 300 hehe para lang po magpantay yung values
        mean_zenith = sum(adjusted_zenith) / len(adjusted_zenith)
        return mean_zenith
    
    def get_mean_time(self):
        mean_time = sum(self.time) / len(self.time)
        return mean_time

class AzimuthCalc(AzimuthCalculation):
    def __init__ (self,time, HCR, zenith/altitude, latitude, parallax_corr)
    super().__init__(self,time, HCR, zenith/altitude)
        self.latitude = latitude
        self.parallax_corr = parallax_corr
    def correct_NPD (self):
        pass
    def calculate_azimuth (self):
        pass
"""


# 2. Discuss the three (3) types of control structures.
""" 
There are three types of control structures, namely: sequence structure, selection structure, and  repitition structure. 
In sequence structure, it just executes actions in the order they are written. When all lines are read and executed, the code stops running. 
This is the simplest form of control structure. For example, if we want to simply get the latitude and departure of lines, we can use this structure.

distance = int(input(distance: ))
azimuth = int (input(azimuth in dd: ))

latitude = -distance*cos(azimuth)
departure = -distance*sin(azimuth)

print (latitude)
print (departure)

On the other hand, selection structure allows different actions to be executed based on specific conditions. It uses if, elif (else if), 
and else statements to determine which block of code to execute based on the truth value of specified conditions.
For example, if we want to convert azimuth to bearing, we can use this type of structure. 

azimuth = int (input(azimuth in dd: ))
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

Lastly, repitition structure allows actions to be repeated until a certain condition is met. It typically uses for loops for a predetermined number of iterations 
or while loops for indefinite iterations until a condition becomes false.

Example using for loop, if we want to get the summation of distance: 

distances = [100, 200, 300, 400]
total_distance = 0
for distance in distances:
    total_distance += distance

If we want to classify a parcel of land, we can use while loop:

areaInHectares = [2, 3, 4]
parcelOfLand = 1
i = 0
while i < len(areaInHectares):
    if areaInHectares[i] > parcelOfLand:
        print("The land is not residential")
        break
    i += 1
"""


# 3. What is Operation Overloading in OOP? 

"""
In object-oriented programming, operation overloading is a means to define several methods or functions under the same name, each with an independent implementation 
depending on the kinds of operands or arguments that are used. This enables operators or functions to exhibit different actions depending upon 
the context or categories of data they process.
For example,

class Line:
    def __init__ (self, distance, azimuth):
    self.distance = distance
    self.azimuth = azimuth

    def __add__(self, other):
        total_distance = self.distance + other.distance
        total_azimuth = self.azimuth + other.azimuth
        return Line(total_distance, total_azimuth)
    
    def getLat(self):
        latitude = -self.distance * math.cos(math.radians(self.azimuth))
        return latitude

lineAB = Line (20, 90)
lineBC = Line (30, 180)

totalLat = lineAB + lineBC

"""


# 4 You are creating a surveying app called SurveyMaster, designed to help geodetic engineers in their survey calculations. What components in React Native/Expo will be useful in building the app?
"""
View - This contains everything users see, like text, input boxes, buttons, and a scrolling menu. It organizes how survey data and results are shown.
Text - The guidelines to use the SurveyMaster, the results, and other text elements are included in this component.
Text Input - This will allow  geodetic engineers to input the values (like distances, bearings, etc) for their survey calculation.
Button - The one the users can press to perform calculations or other actions. 
Scroll View -  Helps navigate long survey calculations that can't fit on one screen, ensuring all data is accessible.
Style Sheet - Makes SurveyMaster look good and consistent by setting styles for text, buttons, and other elements, improving how it feels to use.

"""


# 5 Give five (5) main differences in the syntax of Python and JavaScript.
"""
- creating functions

Python: 
def getLat (distance, azimuth):
    lat = -distance*cos(azimuth)
    return lat

JS:
function getLat (distance, azimuth){
    let lat = -distance*cos(azimuth);
    return lat;
}

- declaring a variable 

Python: 
distance = 300

JS:
var distance = 300 (traditional method)
let distance = 300 (block scope)
const distance = 300 (if constant)

- output

Python: print ('Pasadong final exam cutie')
JS: console.log('Pasadong final exam cutie')

- comments

Python: 
# Single-line comment
"""
Multi-line comment 
"""
JS:
// Single-line comment
/*
Multi-line comment
*/

- logical operators

Python: and or not
JS: && || !


"""
