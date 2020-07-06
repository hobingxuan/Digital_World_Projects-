# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:28:31 2020

@author: hobin
"""

#W4 Cohort Qn 2

def compound_value_months(amt, rate, months):
    x = 0
    for i in range(months):
        x = ((amt + x) *(1 + rate/12))
    return round(x,2)


#W4 Cohort Qn 3
    
import math

def find_average(lst):
    
    new_list = []
    total = 0
    n = 0
    
    for i in lst:
        if i != []:
            total += sum(i)
            n += len(i)
            sub_average = sum(i) / len(i)
            new_list.append(sub_average)
            total_average = total / n
        else:
            new_list.append(0)
        
    return new_list, total_average

#W4 Cohort Qn 4

def transpose_matrix(matrix):
    transpose_result = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
    for x in range(len(matrix)):
               for y in range (len(matrix[0])):
                   transpose_result [y][x] = matrix [x][y]
    return transpose_result

def transpose_row(matrix):
    transposed = []
    num_col = len(matrix[0])
    
    for i in range(num_col):                 #loop over columns
        transposed_row = []
        
        for row in matrix:                     #loop over rows
            transposed_row.append(row[i])
        
        transposed.append(transposed_row)
        
    return transposed


#W4 Cohort Qn 5

def get_details(name, key, lst):
    
    for stalker in lst:
        if stalker["name"] == name:
            return stalker[key]
        
        else: 
            output = None
    return output

#W4 Cohort Qn 6

def get_base_counts(dna):
    output = {'A' : 0 , 'C': 0 , 'G' : 0 , 'T': 0}
    for count in dna:
        if count == 'A':
            output['A'] += 1
        elif count == 'C':
            output['C'] += 1
        elif count == 'G':
            output['G'] += 1
        elif count == 'T':
            output['T'] += 1
        else:
          return "The input DNA string is invalid"
    return output

# W4 2D Qn 1           
def mgrid2d(xstart, xend, xpoints, ystart, yend, ypoints):
    # initialize a list to store the grid points that will be returned
    xr=[]
    yr=[]
    
    # initialize the first x value
    xval = xstart
    
    # initialize a variable to count the number of x points
    xcount = 0
    
    # Calculate the step size for x and y, replace None with the right expression
    xstep = (xend - xstart) / (xpoints - 1)
    ystep = (yend - ystart) / (ypoints - 1)
    
    while xcount < xpoints:
        # initialize the first y value, replace None with the right value
        yval = ystart
        
        # initialize the variable to count the number of y points, replace None with the right value
        ycount = 0
        
        # initialize temporary lists
        xrow = []
        yrow = []
        
        while ycount < ypoints:
            # write code to add the current x value to the temporary x list
            xrow.append(xval)
        
            # write code to add the current y value to the temporary y list
            yval.append(yval)
        
            # increase the y value by the step size in y
            yval += ystep 
        
            # increase the counter for the number of y points
            ycount += 1
            
        # Add the temporary x list to the final x list
        xr.append(xrow)
    
        # Add the temporary y list to the final y list
        yr.append(yrow)
    
        # increase x value by the step size in x
        xval = xval + xstep
    
        # increase the counter for the number of x points
        xcount += 1
        
    return xr, yr


# W4 2D Qn 2

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

# W4 HW1a
def f_to_c(f):
    c = round((f - 32) * (5/9), 1)
    return c

def f_to_c_approx(f):
    c_approx = round((f - 30) / 2, 1)
    return c_approx

def get_conversion_table_a():
    
    conv_table = []
    
    for f  in range(0, 101, 10):
        conv_table.append([f, f_to_c(f), f_to_c_approx(f)])  
        
    return conv_table

def transpose_matrix(matrix):
    return [[row[column] for row in matrix] for column in range(len(matrix[0]))]

print(transpose_matrix(get_conversion_table_a()))
# W4 HW1b

def f_to_c(f):
    c = round((f - 32) * (5/9), 1)
    return c

def f_to_c_approx(f):
    c_approx = round((f - 30) / 2, 1)
    return c_approx

def get_conversion_table_b():
    f_table = []
    c_table = []
    c_approx_table = []
    conv_table = []
    
    for f  in range(0, 101, 10):
        f_table.append(f)
        c_table.append(f_to_c(f))
        c_approx_table.append(f_to_c_approx(f))
    
    conv_table.append(f_table) 
    conv_table.append(c_table)
    conv_table.append(c_approx_table) 
    
    return conv_table
print(get_conversion_table_a())
print(get_conversion_table_b())
# W4 HW2

def max_list(inlist):
    max_list = []
    for term in inlist:
        maximum = 0
        for i in term:
            if i == term[0]:
                maximum = i
            if i >= maximum:
                maximum = i
    
        max_list.append(maximum)
    return max_list


# W4 HW3
def multiplication_table(n):
    if n >= 1:
        times_table = [[row * column for row in range(1, n + 1)] for column in range(1, n + 1)]
        return times_table
    else:
        return None

   
# W4 HW Q4

def most_frequent(lst):
    dictionary = {}
    for i in lst:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    highest_n_freq = 0
    
    for n, freq in dictionary.items():
        if freq > highest_n_freq:
            output = []
            highest_n_freq = freq
            output.append(n)
        elif freq == highest_n_freq:
            highest_n_freq = n
            output.append(n)
    
    return output

# W4 HW Q5

def diff(p):
    differential_dict = {}
    for i, power in p.items():
        if i >= 1:
            differential_dict[i-1] = i * power
    return differential_dict