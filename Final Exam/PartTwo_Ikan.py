"""
Chelzy L. Ikan
2023-03942
"""
from math import sqrt

class Point: #This class is made to represent a point in 2d space.
    def __init__(self, x, y): 
        """
        Initializes a point with x and y coordinate.
        """

        self.x = x
        self.y = y

    def display (self): 
        """
        Presents our coordinate in (x,y) format.
        """

        print ((self.x, self.y))

    def distance_to (self, other): 
        """
        Calculates the distance between points using the pythagorean theorem.
        Input - (x1, y1) and (x2, y2)
        Output - Distance 
        """

        distance = sqrt ((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance

class SurveyPoint (Point): #A subclass of Point to represent a point in 3d space
    def __init__(self, x, y, z):
        """
        Initializes a point with x, y, and z coordinate.
        """

        super().__init__(x, y)
        self.z = z

    def display(self):
        """
        Presents our 3d coordinate in (x,y,z) format.
        """

        print ((self.x, self.y, self.z))

    def distance_to(self, other):
        """
        Calculates the distance between points (x, y, z) using the pythagorean theorem.
        Input - (x1, y1, z1) and (x2, y2, z2)
        Output - Distance 
        """

        distance = sqrt ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
        return distance
    
    def horizontal_distance (self, other):
        """
        Calculates the horizontal distance between points (z excluded) using the pythagorean theorem.
        Input - (x1, y1) and (x2, y2)
        Output - Distance 
        """

        horizontal_distance = sqrt ((self.x - other.x)**2 + (self.y - other.y)**2)
        return horizontal_distance
    
    def __add__(self, other):
        """
        Overloads the addition operator + in the SurveyPoint class to add the coordinates of two SurveyPoint objects.
        Input - (x1, y1, z1) and (x2, y2, z2)
        Output - (x1+x2, y1+y2, z1+z2)
        """

        new_x = self.x + other.x
        new_y = self.y+ other.y
        new_z = self.z+ other.z
        return SurveyPoint (new_x, new_y, new_z)
    
    # The ff methods will allow us to access private attributes.
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z
    
# Example: 
if __name__ == "__main__":
    sp1 = SurveyPoint(3, 4, 5)
    sp2 = SurveyPoint(6, 8, 10)
    
    sp1.display()  
    sp2.display() 
    
    distance_3d = sp1.distance_to(sp2)
    print('Distance in 3D:', round(distance_3d, 2)) 
    
    distance_horizontal = sp1.horizontal_distance(sp2)
    print('Horizontal Distance:', round (distance_horizontal,2))  
    
    sp3 = sp1 + sp2
    sp3.display()  
    
    print('x coordinate:',(sp1.get_x())) 
    print('y coordinate:',(sp1.get_y()))  
    print('z coordinate:',(sp1.get_z())) 