# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:29:51 2020

@author: hobin
"""
"""
#W5 C Q1
import random

craps=set([2,3,12])
naturals=set([7,11])

def roll_two_dices():
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    return n1 , n2

def print_lose():
    print("You lose")

def print_win():
    print("You win")

def print_point(p):
    print("Your points are", p)

def is_craps(n):
    if n in craps:   #cannot be == if not it will only be true if it matches all values in the craps set
        return True
    else:
        return False
    

def is_naturals(n):
    if n in naturals:   #cannot be == if not it will only be true if it matches all values in the naturals set
        return True
    else:
        return False
    


# ATTENTION!
# You shouldn't need to edit the function below

def play_craps():
    point=-1
    while True:
        n1,n2=roll_two_dices()
        sumn=n1+n2
        print ('You rolled %d + %d = %d'%(n1,n2,sumn))   #initial points obtained here
        if point==-1:              #At the initialisation of point == -1 (see line 29)
            if is_craps(sumn):  #if the sum is in the set of craps
                print_lose()     #then it is an immediate loss
                return 0
            elif is_naturals(sumn):   #if the sum is in the set of naturals
                print_win()     #then it is an immediate  win
                return 1
            point=sumn
            print_point(point)
        else:
            if sumn==7:
                print_lose()
                return 0
            elif sumn==point:
                print_win()
                return 1   #goal of the game is to keep rolling dice until the sum == points obtained


#W5 C Q2

def leap_year(year):
    if year % 4 != 0.0:
        return False
    elif year % 100 != 0.0:
        return True
    elif year % 400 != 0.0:
        return False
    else:
        return False

def day_of_week_jan1(year):
    if year > 1800 and year < 2099:
        d = (1 + (5 * ((year - 1) % 4)) + (4 *((year - 1) % 100)) + 6 * ((year - 1) % 400))%7

def num_days_in_month(month_num, leap_year):
    if month_num in range(0,13):
        if leap_year(leap_year):
            if month_num == 2:
                return 29
            else: 
                return (28 + (month_num + (month_num / 8⌋) % 2) + (2 % month_num) + 2 * (1 / month_num))
        else:
            if month_num == 2:
                return 28
            else:
                return (28 + (month_num + (month_num / 8⌋) % 2) + (2 % month_num) + 2 * (1 / month_num))           

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    

def construct_cal_year(year):
    pass

def display_calendar(year):
    pass


def leap_year(year):
    if year % 4 != 0.0:
        return False
    elif year % 100 != 0.0:
        return True
    elif year % 400 != 0.0:
        return False
    else:
        return True

def day_of_week_jan1(year):
    if year > 1800 and year < 2099:
        d = (1 + (5 * ((year - 1) % 4)) + (4 *((year - 1) % 100)) + 6 * ((year - 1) % 400))%7
        return d

def num_days_in_month(month_num, leap_year):
    if month_num in range(0,13):
        if month_num in [1 , 3 , 5 , 7 , 8 , 10 , 12]:
            return 31
        elif leap_year(leap_year):
            if month_num == 2:
                return 29
        elif month_num in [2 , 4 , 6 , 9, 11]:
            return 30
        else:
            return 28     

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    week_1 = " "
    week_2 = " "
    week_3 = " "
    week_4 = " "
    month_name = {
        1: January
        2: February
        3: March
        4: April
        5: May
        6: June
        7: July
        8: August
        9: September
        10: October
        11: November
        12: December}
    if day_of_week_jan1 =
    
        
    
    
    

def construct_cal_year(year):
    pass

def display_calendar(year):


    pass    



a = [1,2,3,4]
" ".join(a) == "1 2 3 4"

quantity = 10
animal = "duck"
message = "there are {0:3d} {1:>20s} in the zoo".format(quantity, animal)
print (message)


def leap_year(year):
    if year == 1860:
        return True
    elif year % 4 != 0:
        return False
    elif year % 100 != 0.0:
        return True
    elif year % 400 != 0.0:
        return False
    else:
        return True

def day_of_week_jan1(year):
    if year > 1800 and year < 2099:
        d = (1 + (5 * ((year - 1) % 4)) + (4 *((year - 1) % 100)) + 6 * ((year - 1) % 400))%7
        return d

def num_days_in_month(month_num, leap_year):
    if month_num in range(0,13):
        if month_num in [1 , 3 , 5 , 7 , 8 , 10 , 12]:
            return 31
        elif month_num in [4 , 6 , 9, 11]:
            return 30
        elif leap_year == True:
            return 29
        else:
            return 28     

def get_month_name(month_num):
    
    month_name = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'}
    
    return month_name[month_num]
    
def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    cal = [get_month_name(month_num)]

    week_string = "   " * int(first_day_of_month)
    
    #now adjust the indices to take care of the week strings
    first_day = first_day_of_month + 1
    last_day = num_days_in_month + first_day
    
    for i in range(first_day, last_day):
        date = i - first_day_of_month
        week_string = week_string + '{:3d}'.format(date) #creates 3 spaces for each entry
        
        if (i % 7 == 0):
            #print(week_string)
            cal.append(week_string)
            week_string = ""  #makes string empty to print the consequent entries
            
    #print(week_string) #prints the remaining entries outside the if condition Eg: 29 , 30 , 31
    #append last week's string only if it is not empty
    if (len(week_string) > 0):
        cal.append(week_string)
    
    return cal

def construct_cal_year(year):
    cal_year = []
    cal_year.append(year)
    start_day = day_of_week_jan1(year)
    for month_num in range(1 , 13):
        cal_month = construct_cal_month(month_num, start_day, num_days_in_month(month_num, leap_year))
        cal_year.append(cal_month)
        if len(cal_year[-1][-1]) != 21:
            start_day = int(len(cal_year[-1][-1])/3) 
        else:
            start_day = int(0) 
    return cal_year
                        

def display_calendar(year):
    day_legend = "  S  M  T  W  T  F  S"
    calendar= ""
    for month_index in range(1 , 13):
        if month_index != 1 and month_index != 13:
            calendar += "\n"
        for row_index in range(len(construct_cal_year(year)[month_index])):
            if row_index == 1:
                calendar += day_legend + "\n"
                calendar += str(construct_cal_year(year)[month_index][row_index]).strip('[]') + "\n"
            elif row_index == len(construct_cal_year(year)[month_index])-1 and month_index == 12:
                calendar += str(construct_cal_year(year)[month_index][row_index]).strip('[]')
            else:
                calendar += str(construct_cal_year(year)[month_index][row_index]).strip('[]') + "\n"
    return calendar
                    
                
print(display_calendar(1860))


#W5 Cohort Qn 3

def fact_rec(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fact_rec (n - 1) * n  #recursion
    
#ternary operator
a = 2
is_a_even = a % 2 == 0
fruit = 'apple' if is_a_even else 'orange' #compressed version of if else statements
print(fruit)

b = []
for i in range(10):
    b.append(i / 10)
print(b)

# List Comprehension
b = [i/10 for i in range(10)] #compressed version of for loop


# Recursion (Function calls itself with a stopping feature)

total = 0
n =  100
for i in range (1 , n + 1):
    total = total + i

print(total)


def total(n):
    if (n ==1):
        return 1
    else:
        return total(n - 1) + n # total(5) becomes 5 + total(4) which then becomes 5 + 4 + total(3) so on and so forth
                                # represent the problem as a smaller version of itself

print(total(5)) 

 
# W5 HW 1:
# NB: you do not need to submit the 'get_data' function

def extract_values(values):
    output =  tuple(map(int, values.split()))
    return output
    

def calc_ratios(values):
    output1 = values[0]
    output2 = values[1]
    if output2 == 0:
        return None
    else:
        result = output1 / output2
    return result


# W5 HW 2:

# NB: the following line imports the 'display_calendar', 'lear_year', etc. functions
# (see the problem sheet PDF)
# DO NOT delete hw2_others.pyc from Vocareum :-)
from hw2_others import *

# You should ONLY submit the 'display_calendar_modified' function

def display_calendar_modified(year, month):
    if year == None:
        return display_calendar()
    else:      
        day_legend = "  S  M  T  W  T  F  S"
        calendar= ""
        if month in range(1 , 13):
                for row_index in range(len(construct_cal_year(year)[month])):
                    if row_index == 1:
                        calendar += day_legend + "\n"
                        calendar += str(construct_cal_year(year)[month][row_index]).strip('[]') + "\n"
                    elif row_index == len(construct_cal_year(year)[month])-1:
                        calendar += str(construct_cal_year(year)[month][row_index]).strip('[]')
                    else:
                        calendar += str(construct_cal_year(year)[month][row_index]).strip('[]') + "\n"
                return calendar
        else:
            return display_calendar(year)
"""
# W5 2D:

import numpy as np
import scipy.constants as c


def spherical_to_cartesian(r,theta,phi):
    base = r * np.sin(theta)
    x = round(base * np.cos(phi), 5)
    y = round(r * np.sin(phi), 5)
    z = round(r * np.cos(theta), 5)
    return x , y , z

def cartesian_to_spherical(x, y, z):
    r = round(np.sqrt(x**2 + y**2 + z**2), 5)
    theta = round(np.arccos(z/r), 5)
    if x == 0.0:
        if y == 0.0:
            p = 0.0
        else:
            p = np.inf
    else:
        p = y/x      
    
    phi = round(np.arctan(p), 5)
    return r , theta , phi



def angular_wave_func(m,l,theta,phi):
    if  l ==0 :
        Y = np.sqrt(1/(4*c.pi))
        
    elif l == 1:
        if m == 1:
            Y = - np.sqrt(3/(8*c.pi)) * np.sin(theta) * np.exp(1j * phi)
        elif m == 0:
            Y = np.sqrt(3/(4*c.pi)) * np.cos(theta)
        elif m == -1:
            Y = np.sqrt(3/(8*c.pi)) * np.sin(theta) * np.exp(-1j * phi)    
            
    elif l == 2:
        if m == 2:
            Y= np.sqrt(15/(32*c.pi)) * (np.sin(theta)) ** 2 * np.exp(1j * 2 * phi)
        elif m == 1:
            Y= - np.sqrt(15/(8*c.pi)) * np.sin(theta) * np.cos(theta) * np.exp(1j * phi)
        elif m == 0:
            Y= np.sqrt(5/(16*c.pi)) * ((3 * (np.cos(theta))**2) -1)         
        elif m == -1:
            Y = np.sqrt(15/(8*c.pi)) * np.sin(theta) * np.cos(theta) * np.exp(-1j * phi)
        elif m == -2:
            Y = np.sqrt(15/(32*c.pi)) * (np.sin(theta)) ** 2 * np.exp(1j * -2 * phi)
        
    elif l == 3:
        if m == 3:
           Y = - np.sqrt(35/(64*c.pi)) * (np.sin(theta)) ** 3 * np.exp(1j * 3 * phi) 
        
        elif m == 2:
            Y= (np.sqrt(105/(32*c.pi))) * (np.cos(theta)) * (np.sin(theta)**2) * (np.exp(1j*2*phi))
        elif m == 1:
            Y = -(np.sqrt(21/(64*c.pi))) * (np.sin(theta)) * ((5*np.cos(theta)**2)-1) * (np.exp(1j*phi))
        elif m == 0:
            Y= (np.sqrt(7/(16*c.pi))) * ((5*(np.cos(theta))**3) - (3*np.cos(theta)))
        elif m == -1:
            Y = (np.sqrt(21/(64*c.pi))) * (np.sin(theta)) * ((5*np.cos(theta)**2)-1) * (np.exp(-1j*phi))   
        elif m == -2:
            Y = (np.sqrt(105/(32*c.pi))) * (np.cos(theta)) * ((np.sin(theta)**2)) * (np.exp(-1j*2*phi))   
        elif m == -3:
            Y = np.sqrt(35/(64*c.pi)) * (np.sin(theta)) ** 3 * np.exp(1j * -3 * phi) 
                       
    return Y



def radial_wave_func(n,l,r):
    a=c.physical_constants['Bohr radius'][0]
    if  n == 1:
        R = (2*a**(-3/2)) * (np.exp(-r/a))
        
    elif n == 2:
        if l == 0:
            R = (1/np.sqrt(2)) * (a ** (-3/2)) * (1-(r/(2 * a))) * np.exp(-r/(2 * a))
        elif l == 1:
            R = (1/np.sqrt(24)) * (a ** (-3/2)) * (r/a) * np.exp(-r/(2 * a))
            
    elif n == 3:
        if l == 0:
            R = (2/(81 * np.sqrt(3))) * (a ** (-3/2)) * (27-18 * (r/a) + 2 * (r/a))
        elif l == 1:
            R = (8/(27 * np.sqrt(6))) * (a ** (-3/2)) * (r/a) * (1-(r/(6*a))) * np.exp(-r/ (3 * a))
        elif l ==2:
            R = (4/(81 * np.sqrt(30))) * (a ** (-3/2)) * (r/a) ** 2 *np.exp(-r/(3*a))
            
    elif n == 4:
        if l == 0:
            R = (1/4) * (a(-3/2)) * (1-(3/4) * (r/a) + (1/8) * (r/a)**2 - (1/192) * (r/a) ** 3) * np.exp((-r/4 * a))
        elif l == 1:
            R = (np.sqrt(5) / (16*np.sqrt(3))) * (a(-3/2)) * (r/a) * (1-(1/4) * (r/a) + (1/80) * (r/a)**2) * np.exp(-r/(4 * a))
        elif l == 2:
            R = (1/(64 * np.sqrt(5))) * (a(-3/2)) * (r/a)**2 * (1-(1/12) * (r/a)) * np.exp(-r/(4 * a))
        elif l == 3:
            R = (1/(768 * np.sqrt(35))) * (a(-3/2)) * (r/a) ** 3 * np.exp(-r/(4 * a))
    
    radial = R/(a**(-3/2))
            
    return round(radial, 5)

def mgrid3d(xstart, xend, xpoints, 
            ystart, yend, ypoints, 
            zstart, zend, zpoints):
    xr = []
    yr = []
    zr = []
    x_val = xstart
    xcount = 0

    # calculate the step size for each axis
    x_step = (xend - xstart) / (xpoints - 1)
    y_step = (yend - ystart) / (ypoints - 1)
    z_step = (zend - zstart) / (zpoints - 1)
    
    while xcount < xpoints:
        # initialize y points
        # create temporary variable to store x, y and z list
        y_val = ystart
        ycount = 0
        x_list = []
        y_list = []
        z_list = []
    
        while ycount < ypoints:
            # initialize z points
            # create temporary variable to store the inner x, y, and z list
            z_val = zstart
            zcount = 0
            x_list2 = []
            y_list2 = []
            z_list2 = []
            
            while zcount < zpoints:
                # add the points x, y, and z to the inner most list
                x_list2.append(x_val)
                y_list2.append(y_val)
                z_list2.append(z_val)
            
                # increase z point
                z_val += z_step
                zcount += 1
                
            # add the inner most lists to the second lists
            x_list.append(x_list2)
            y_list.append(y_list2)
            z_list.append(z_list2)
        
            # increase y point
            y_val += y_step
            ycount += 1
            
        # add the second lists to the returned lists
        xr.append(x_list)
        yr.append(y_list)
        zr.append(z_list)
    
        # increase x point
        x_val += x_step
        xcount += 1
        
    return ([xr, yr, zr])


def xmag(c):               # function to find absolute value of complex number c
    mag_real = np.real(c)
    mag_imag = np.imag(c)
    return np.sqrt(mag_real**2 + mag_imag**2)

def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    grids_in_radial = mgrid3d(-roa, roa, Nx, -roa, roa, Ny,-roa, roa, Nz)
    
    a=c.physical_constants['Bohr radius'][0]  #extract Bohr's Radius from Scipy
    v_func = np.vectorize(round)
    v_cs = np.vectorize(cartesian_to_spherical) #vectorise function from cartesian to spherical
    v_angular = np.vectorize(angular_wave_func) #vectorise angular wave function
    v_radial = np.vectorize(radial_wave_func) #vectorise radial wave function
    v_mag = np.vectorize(xmag)  #vectorise the absolute value of complex number c
    
    r,theta,phi = v_cs(grids_in_radial[0],grids_in_radial[1],grids_in_radial[2])
    angular = v_angular(m,l,theta,phi)
    angular2 = v_angular(-m,l,theta,phi)
    radial = v_radial(n,l,r*a)
    
    if m < 0:
        Y = 1j/(2)**0.5*(angular-(-1)**m*angular2)
    elif m == 0:
        Y = angular
    else:
        Y = 1/2**0.5*(angular2+(-1)**m*angular)
    dens = v_mag((radial*Y))**2
    grids_in_radial = v_func(grids_in_radial,5)
    dens = v_func(dens,5)
    return (grids_in_radial[0],grids_in_radial[1],grids_in_radial[2],dens)

print('Test ')
x,y,z,mag=hydrogen_wave_func(4,3,-3,-40,10,10,10)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)
print (x,y,z,mag)
x.dump('x_test.dat')
y.dump('y_test.dat')
z.dump('z_test.dat')
mag.dump('den_test.dat')
