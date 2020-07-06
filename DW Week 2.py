# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:19:03 2020

@author: hobin
"""

class Coordinate: 
    x = 9
    y = 4
    
p1 = Coordinate ()
p2 = Coordinate ()

p2.x = 4
p1.x = 7

print(p1.x , p2.y)

print(type(Coordinate))

print(17-3*7//4+1)


Makes the code end on the same line instead of a new line and prints the next x value beside the previous x value

x = 3
print(x, end = '')
x = x+2
print(x)
  
student_name = input(str("Name: "))
student_id = input("Student ID: ")
qm = int(input("Quiz Marks: "))
pm = int(input("Project Marks: "))
fp = int(input("Final Paper Marks: "))

average_marks = round((qm + pm + fp) / 3 , 2)

if average_marks > 50:
    print ("hello " , student_name , ", student ID : " , student_id , ", your average marks is " , average_marks , ". You have passed the module.") 
else:
    print("hello " , student_name , ", student ID : " , student_id , ", your average marks is " , average_marks , ". You have failed the module.")
    
    
i = 0
while i < 2: 

    student_name = input(str("Name: "))
    student_id = input("Student ID: ")
    qm = int(input("Quiz Marks: "))
    pm = int(input("Project Marks: "))
    fp = int(input("Final Paper Marks: "))
    
    average_marks = round((qm + pm + fp) / 3 , 2)
    
    if 0 <= average_marks < 60:
        print ("hello " , student_name , ", student ID : " , student_id , ", your average marks is " , average_marks , ". Your grade is F.") 
    elif 60 <= average_marks < 70:
        print("hello " , student_name , ", student ID : " , student_id , ", your average marks is " , average_marks , ". Your grade is D.")
    elif 70 <= average_marks < 80:
        print("hello " , student_name , ", student ID : " , student_id , ", your average marks is " , average_marks , ". Your grade is C.")
    elif 80 <= average_marks < 90:
        print("hello " , student_name , ", student ID : " , student_id , ", your average marks is " , average_marks , ". Your grade is B.")
    elif 90 <= average_marks < 100:
        print("hello " , student_name , ", student ID : " , student_id , ", your average marks is " , average_marks , ". Your grade is A.")
    else:
        print("Your results are invalid.")
    i += 1

def position_velocity(v0, t):
    g = 9.81
    y = v0 * t - 0.5 * g * t**2
    v= v0 - g * t
    return round(y , 1) , round(v , 1)
print(position_velocity(5.0, 10.0)) 


def bmi(weight, height):    
    hc = height/100
    bmi = round((weight / hc**2) , 1)
    return bmi
print(bmi(60,120))

from math import sqrt

class Coordinate:
    x = 0.0
    y = 0.0

def area_of_triangle(p1,p2,p3):
    side1 = sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    side2 = sqrt((p2.x-p3.x)**2 + (p2.y-p3.y)**2)
    side3 = sqrt((p3.x-p1.x)**2 + (p3.y-p1.y)**2)
    s = (side1 + side2 + side3) / 2
    area = sqrt(s * (s - side1)*(s - side2)*(s - side3))
    area_round = round(area, 2)
    return area_round


print("Test Case 1") 
p1=Coordinate()
p1.x=1.5 
p1.y=-3.4 
p2=Coordinate() 
p2.x=4.6 
p2.y=5 
p3=Coordinate() 
p3.x=9.5 
p3.y=-3.4
ans=area_of_triangle(p1,p2,p3) 
print(ans)    


from math import sqrt

class Coordinate:
    x = 0.0
    y = 0.0

p1.x = float(input("Enter x coordinate of the first point of a triangle: "))
p1.y = float(input("Enter y coordinate of the first point of a triangle: "))
p2.x = float(input("Enter x coordinate of the second point of a triangle: "))
p2.y = float(input("Enter y coordinate of the second point of a triangle: "))
p3.x = float(input("Enter x coordinate of the third point of a triangle: "))
p3.y = float(input("Enter y coordinate of the third point of a triangle: "))


side1 = sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
side2 = sqrt((p2.x-p3.x)**2 + (p2.y-p3.y)**2)
side3 = sqrt((p3.x-p1.x)**2 + (p3.y-p1.y)**2)
s = (side1 + side2 + side3) / 2
area = sqrt(s * (s - side1)*(s - side2)*(s - side3))
area_round = round(area, 2)
print("The area of the triangle is ", area_round)


import math

class Coordinate:
    x = 0.0
    y = 0.0

def is_in_square(square1, side1, square2, side2):
    r = False
    t = False
    length_cover = (side1/2 + side2/2)
    if length_cover > abs(square1.x - square2.x):
        r = True
    else:
        r = False
    if length_cover > abs(square1.y - square2.y):
        t = True
    else: 
        t = False
    if ((r == True) and (t == True)):
        return True
    else:
        return False

s1 = Coordinate()
s1.x, s1.y = 10, 10
s2 = Coordinate()
s2.x, s2.y = 20, 10
print(is_in_square(s1, 5, s2, 4))