# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:16:25 2020

@author: hobin
"""
"""
a = [1,2,3,4,5,6,7,8]
a = a[2:7:2]
print(a)
"""
"""
investment = int(input("Enter investment amount: "))
interest = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

total = round((investment * (1 + interest/1200)**(years*12)), 2)

print("Accumulated value is ", total)


def is_larger(n1,n2):
    if n1 > n2:
        return True
    else:
        return False
print(is_larger(2,2)) 


def check_value(n1,n2,n3,x):
    if x > n1 and x > n2 and x < n3:
        return True
    else:
        return False

print("Test case 2: check_value(10,4,8,7)") 
print("ans = False") 
ans=check_value(10,4,8,7) 
print(ans)

# W3 Cohort Q1

def list_sum(ls):
    num_values = len(ls)
    if num_values == 0:
        return 0.0
    else:
        i = 0
        ans = 0 
        while i < num_values:
            ans += ls[i]
            i +=1
        return ans

print("Test case 3: []") 
ans=list_sum([]) 
print(ans)

# W3 Cohort Q2

def minmax_in_list(values):
    num_values = len(values)
    if num_values == 0.0:
        return None, None
    else:
        i = 0
        minimum = values[0]
        maximum = values[0]
        while i < num_values:
            if values[i] > maximum:
                maximum = values[i]
            if values[i] < minimum:
                minimum = values[i]
            i +=1
        return minimum, maximum
    
print("Test case 1: [1,1,3,0]") 
ans=minmax_in_list([1,1,3,0]) 
print(ans)


#W3 Cohort Q3

def is_palindrome(values):
    value = str(values)
    num_values = len(value)
    if num_values == 0:
        result = True
    else:
        i = 0
        last_value = num_values - 1
        while i < (num_values/2):
            if (value[i] == value[last_value]):
                i +=1
                result = True
            else:
                result = False 
        return result

print("Test case 1: 1") 
ans=is_palindrome(1) 
print(ans)


for i in range(20):
    if i == 10:
        continue
    print(i)
    ## this excludes the entry when i = 10

sqrt(16)
       
            
a = [1,2,3,4,5,6,7,8]
a = a[2:7:2]
print(a)                
        
            
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.show()


plt.plot([1, 2, 3, 4], [1, 2, 3, 4],bo)
plt.show()


# W3 HW1

def get_even_list(ls):
    n = len(ls)
    if n == 0.0:
        return None
    else:
        i = 0
        while i < n:
            if (ls[i]) % 2 != 0:
                ls.pop(i)
            else:
                i += 1
        return ls

print("get_even_list([1,2,3,4,5])") 
ans=get_even_list([1,2,3,4,5]) 
print(ans)

# W3 HW2

def is_prime(n):
    if 0 < n < 3:
        return True
    else:
        i = 2
        while i < n:
            if n % i != 0.0:
                i += 1
            else:
                return False
        return True
        

print("is_prime(21)") 
ans=is_prime(21) 
print(ans)


# W3 HW3 

import math
import numpy as np

def approx_ode(h,t0,y0,tn):
    t = t0
    y = y0
    while t < tn:
        dy_dt = 3 + np.exp(-1 * t) - 0.5*y
        y += h * dy_dt
        t = round(t + h, 1)
    return y

print('approx_ode(0.1, 0, 1, 5)') 
ans = approx_ode(0.1, 0, 1, 5) 
print('Output: ', ans) 



#W3 Exercise 4
def gcd(n1,n2):
    if n1 < 0 or n2 < 0:
        return None
    else:
        i = 2.0
        ans = 1.0
        while i <= n1 or i <= n2:
            if n1 % i == 0.0 and n2 % i == 0.0:
                ans = i
                i += 1
            else:
                i += 1
        return ans

gcd(144,  201)
print ("GCD is:", gcd(144, 201))

#W3 Ex1

def may_ignore(entry):
    if type(entry) == int:
        return entry + 1
    else: 
        return None
    
print(may_ignore(9.0))

def may_ignore(entry):
    if type(entry) == type(8):
        return entry + 1
    else: 
        return None
    
print(may_ignore(5))

#W3 Exercise 2
def my_reverse(ls):
    reverse = []
    for i in range(len(ls)):
        reverse.append(ls[-i])
    return reverse

print(my_reverse([1,2,3,4]))


def my_reverse(ls):
    return [ls[-i - 1] for i in range(len(ls))]
print(my_reverse([1,2,3,4]))


import math

def approx_pi(n):
    pi_summation = 0
    for k in range(n):
        pi_summation += ((math.factorial(4*k)) * (1103 + (26390 * k)))/(((math.factorial(k))**4) * 396**(4*k))
        pi_recip = ((2 **(3/2))/9801) * pi_summation
        pi = 1 / pi_recip
    return pi
        
print(approx_pi(2000))        


#W3 Exercise 4
def gcd(n1,n2):
    if n1 < 0 or n2 < 0:
        return None
    else:
        i = 2.0
        ans = 1.0
        while i <= n1 or i <= n2:
            if n1 % i == 0.0 and n2 % i == 0.0:
                ans = i
                i += 1
            else:
                i += 1
        return ans

gcd(20001801, 1436445)
print ("GCD is:", gcd(20001801, 1436445))


def gcd(n1,n2):
    if n1 < 0 or n2 < 0:
        return None
    else:
        ls1 =[]
        ls2 = []
        i = 2
        while i < n1 and i < n2:
            if n1 % i == 0:
                ls1.append
                # Not completed

def is_palindrome(values):
    inputs = str(values)
    length = len(inputs)
    half = length/ 2
    if len(inputs) == 0:
        return True
    else:
        i = 0
        last = length - 1
        while i < half:      
            if (inputs[i] == inputs[last]):
                i += 1
                length -= 1
                result = True
            else:
                result = False
        return result
           

print("Test case 1: 1") 
ans=is_palindrome(1) 
print(ans)
print("Test case 2: 22") 
ans=is_palindrome(22) 
print(ans)
print("Test case 3: 12321") 
ans=is_palindrome (12321) 
print(ans)
print("Test case 4: 441232144") 
ans=is_palindrome (441232144) 
print(ans)
print("Test case 5: 441231144") 
ans=is_palindrome (441231144) 
print(ans)
print("Test case 6: 144") 
ans=is_palindrome(144) 
print(ans)
print("Test case 7: 12") 
ans=is_palindrome(12) 
print(ans)
"""
import matplotlib.pyplot as plt
import numpy as np

x = [-5 , -4, -3, -2, -1, 1, 2, 3, 4, 5]
y = []
for i in range(len(x)):
    y_output = (np.exp(x))/(np.exp(x) + 1)
    y.append(y_output)

plt.plot(x,y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Logistic Function')
plt.show()