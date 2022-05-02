# SUPER CLASS PYTHON
# This is an example of a Super Class in python and how to implemented
# I will use as an example geometry and how to get different Area and perimetres of a triangle
# To Calculate the Area we will Use Heron's Formula

import math

######################################################################
# Class and Super Class to calculate the Triangle 
######################################################################

class Triangle(object):

    # Calling Constructor
    def __init__(self,name, s1, s2 ,s3):

        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    
    def setName(self, name):
        self.name = name

    def setDim(self,s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def __str__(self):
        return 'Name: '+self.name+'\nDimensions: '+str(self.s1)+','+str(self.s2)+','+str(self.s3)

    
class Triangle_Formulas(Triangle):

    def calculate_perimeter(self):
        self.pm = 0
        self.pm = self.s1 + self.s2 + self.s3

    def calculate_area(self):
        self.semi_perimeter = (self.s1 + self.s2 + self.s3)/2 
        self.semi = self.semi_perimeter
        self.area= 0
        self.area = math.sqrt(self.semi* (self.semi-self.s1) * (self.semi-self.s2) * (self.semi-self.s3))

    # function to display just the area 
    # because it is not extended
    def display_perimeter(self):
        return self.pm

    def display_area(self):
        return self.area

######################################################################
# Class and Super Class to calculate the Rectangle
######################################################################


class Rectangle(object):

    # Construcctor
    def __init__(self, name, s1, s2):
        self.name = name
        self.s1 = s1
        self.s2 = s2 

    def setName(self,name):
        self.name = name

    def setSides(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def __str__(self):
        return 'Name: '+self.name+'\nDimensions: '+str(self.s1)+','+str(self.s2)

class Rectangle_Formulas(Rectangle):

    def calculate_perimeter(self):
        self.perimeter = 0
        self.perimeter = 2 * (self.s1 + self.s2)

    def calculate_area(self):
        self.area = 0
        self.area = self.s1 * self.s2 

    def display_perimeter(self):
        return self.perimeter
    
    def display_area(self):
        return self.area
    

def main():

    print("Welcome to the program to calculate Area and Perimetres of a Triangle or Square")
    
    option = input("Select your option \nT) Calculate Triangle \nR) Calculate Rectangle \nQ) Quit \nWhat is your option: ").upper()

    while option != "Q":

        if option == "T":
            print("Please introduce the information of the Triangle")
            name = input("Triangle Name: ")
            t1 = int(input ("First Side of the Triangle: "))
            t2 = int(input ("Secoond Side of the Triangle: "))
            t3 = int(input ("Third Side of the Triangle: "))

            p = Triangle_Formulas (name, t1,t2,t3)
            p.calculate_perimeter()
            print(f"The Perimeter of the Triangle of {name} is: {p.display_perimeter()} ")

            p.calculate_area()  
            print(f"The Are of the Triangle of {name} is: {p.display_area()} ")

            print()


            option = input("Select your option \nT) Calculate Triangle \nR) Calculate Rectangle \nQ) Quit \nWhat is your option: ").upper()

        elif option == "R":  

            print("Please introduce the information of the Rectangle")
            name = input("Rectangle Name: ")
            s1 = int(input ("First Side of the Rectangle: "))
            s2 = int(input ("Secoond Side of the Rectangle: ")) 

            r = Rectangle_Formulas(name, s1, s2)
            r.calculate_perimeter()
            print(f"The Perimeter of the Recctangle of {name} is: {r.display_perimeter()} ")

            r.calculate_area()
            print(f"The Are of the Rectangle of {name} is: {r.display_area()} square feet ")

            print()  

            option = input("Select your option \nT) Calculate Triangle \nR) Calculate Rectangle \nQ) Quit \nWhat is your option: ").upper()
 
        elif option == "Q":
            option == "Q"

        else:
            print("Wrong input please")
            option = input("Select your option \nT) Calculate Triangle \nR) Calculate Rectangle \nQ) Quit \nWhat is your option: ").upper()     
        
main()