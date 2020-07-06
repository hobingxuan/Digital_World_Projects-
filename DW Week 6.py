# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:42:51 2020

@author: hobin
"""

# Using Slicing to reverse a string:

a = "apple"
b = a[::-1]
print(b)    
    

# W6 Cohort 1

def reverse(string):
    output = ""
    i = -1
    while abs(i) in range(len(string) +1):
        output = output + string[i]
        i -= 1
    return output


# W6 Cohort 2

def check_password(password):
    length = len(password)
    is_alphanumeric = password.isalnum()
    is_digit = password.isdigit()
    digitcount = 0
    for c in password:
        if c.isdigit() == True:
            digitcount += 1
        else:
            digitcount += 0

    if length < 8:
        return False
    elif is_alphanumeric == False:
        return False
    elif digitcount < 2:
        return False
    else:
        return True

# W6 Cohort 3

def longest_common_prefix(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    output = ""
    if len1 < len2:
        lenx = len1
        x = string1
        leny = len2
        y = string2
    else:
        lenx = len2
        x = string2
        leny = len1
        y = string1
    for i in range(lenx):
        if (x[i] == y[i]):
            output = output + x[i]
        else:
            break    # can be return output too
    return output    # always has to be at this indent otherwise no output will be returned 

print(longest_common_prefix('Nasi_goreng_merah','Nasi_lemak_dengan_ikan'))


# W6 Cohort 4

import math
    
class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    f = open('xy.dat','r') #opens the file and get the file pointer, 'r' means read mode
    minimum = 9e10
    maximum = -100
    for line in f:
        line = line.strip()
        ls = line.split()
        x = float(ls[0])  #cleaning the lines
        y = float(ls[1])  #cleaning the lines
        
        p = Coordinate()  #create object of Coordinate Type
        p.x = x
        p.y = y
        mag = math.sqrt((p.x)**2 + (p.y)**2)
        if mag < minimum:
            minimum = mag
            p_minimum = p
        if mag > maximum:
            maximum = mag
            p_maximum = p
    return p_maximum , p_minimum   

# W6 HW 1

def binary_to_decimal(binstr):
    ans = 0
    power = 0
    for i in str(binstr)[:: -1]:
        ans += int(i) * 2**power
        power += 1
    return ans

def binary_to_decimal(binstr):
    return int(binstr,2)

print(binary_to_decimal(100))


# W6 HW 2
def uncompress(string):
    output = ""
    for i in string:
        if i.isdigit():
            n = int(i)
        else:
            output = output + i*n
    return output

# W6 HW 3
def get_base_counts2(dna):
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    data = list(dna)
    for i in data:
        if i == "A" or i == "C" or i == "G" or i == "T":
            count[i] += 1
        elif i.isupper():
            continue
        else:
            return "The input DNA string is invalid"
    return count

# W6 HW 4
def get_fundamental_constants(f):
    output = {}
    for i in f.readlines():
        i = i.split()
        if len(i) == 3:
            output[i[0]] = float(i[1])    #output[i[0]]  = key , float(i[1]) = value
    return output
    
# W6 HW 5
def total_function(ls):
    total = 0
    for n in ls:
        total += n
    return total


def process_scores(f):
    ls = [float(i) for i in f.read().split()]    #calls the total function 
    return total_function(ls), total_function(ls) / len(ls)

