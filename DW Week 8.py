# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:01:09 2020

@author: hobin


class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def distance_from_origin(self):
		# apply Pythagoras’ Theorem
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Coordinate(3, 4)
print(p.distance_from_origin())	# prints 5 to console


#W8 Cohort 1

class Coordinate:
    def __init__(self, x= 0, y=0):
        self.x = x
        self.y = y
    def magnitude(self):
        return (self.x**2 + self.y**2)** 0.5
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y #better approach
#       if self.x == other.x and self.y == other.y:
 #           return True
  #      else:
   #         return False

#W8 Cohort 2

class Celsius:
    
    def __init__(self, temp =0):
        if temp > -273:
            self._temp = temp
        else:
            self._temp = -273
            
    def to_fahrenheit(self):
        return (self._temp * (9/5) + 32)
    
    def get_temperature(self):
        return self._temp
    
    def set_temperature(self, value):
        if value > -273:
            self._temp = value
        else:
            self._temp = -273
            
    temperature = property(get_temperature, set_temperature)
    
#W8 Cohort 3
 
import time

class StopWatch:
    
    def __init__(self):
        self.start_time = time.time()
        self.end_time = -1
    
    def start(self):                 # start
        self.start_time = time.time()
        self.end_time = -1

    def stop(self):               # stop
        self.end_time = time.time()
    
    def elapsed_time(self):
        if self.end_time == -1:
            return None
        return round(self.end_time - self.start_time, 1)
"""
# W8 Cohort 4 Draft 1 (Not Fully Correct)
class Line:
    
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
        
    def __call__(self,x):
        result = self.c0 + self.c1 * x
        return result
    
    def table(self,L, R, n):
        output = [[],[]]
        x = L
        while x>=L and x<=R:
            output[0].append(round(x,2))
            y = round(self.c0 + (self.c1 * x), 2)
            x += (R-L)/(n-1)
            output[1].append(y)
            tables = ""
            for row in range(len(output[0])):
                tables += ('{0:>10}{1:>10}\n'.format(f'{output[0][row]:.2f}', f'{output[1][row]:.2f}'))
               #table_col1 = str(output[0][row]).strip('[]')
               #table_col1_format = ('{0:>10}'.format(f'{table_col1:.2f}'))
                             #table_col1_format = '{0:.2f}'.format(table_col1_format)
               #table_col2= str(output[1][row]).strip('[]') 
               #table_col2_format = '{:>10}'.format(table_col2)
                             #table_col2_format = '{0:.2f}'.format(table_col2_format)
               #tables += table_col1_format
               #tables += table_col2_format + "\n"
        return tables
                           
 
# W8 Cohort 4 Final
        
class Line:
    
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
        
    def __call__(self,x):
        result = self.c0 + self.c1 * x
        return result
    
    def table(self,L, R, n):
        if n == 0:
            return "Error in printing table"
        else:
            output = [[],[]]
            inc = (R-L)/(n-1)
            x = L
            if L == R:
                tables = ''
                tables += ('{0:>10}{1:>10}\n'.format(f'{L:.2f}', f'{self(L):.2f}'))
                return tables
            else:
                while n>0:
                    output[0].append(x)
                    y = self(x)
                    x += inc
                    output[1].append(y)                   
                    n -= 1
                
                tables = ""
                
                for row in range(len(output[0])):
                    tables += ('{0:>10}{1:>10}\n'.format(f'{output[0][row]:.2f}', f'{output[1][row]:.2f}'))

            
                return tables
        

# Inheritance
                
class Spell:
  def __init__(self, magic_damage):
    self.magic_damage = magic_damage
  
  def cast(self, intelligence):
    return self.magic_damage + intelligence * 1.05

class FireSpell(Spell):
  def __init__(self, fire_damage):
    self.type = "FIRE"  # enhanced the functionality of Spell
    super().__init__(fire_damage)   #super = parent class (Spell)

class IceSpell(Spell):
  def __init__(self, ice_damage):
    self.type = "ICE"   # enhanced the functionality of Spell
    super().__init__(ice_damage)    #super = parent class (Spell)
    
# Chained Inheritance

import random

class Spell:
  def __init__(self, magic_damage):
    self.magic_damage = magic_damage
  
  def cast(self, intelligence):
    return self.magic_damage + intelligence * 1.05

class FireSpell(Spell):
  def __init__(self, fire_damage):
    self.type = "FIRE"  # enhanced the functionality of the Spell
    super().__init__(fire_damage)

class SuperNovaSpell(FireSpell):
  def __init__(self, fire_damage):
    super().__init__(fire_damage * 1.5)   # Invoking parent class- FireSpell which then invoked its parent cell- spell
  
  def cast(self, intelligence):
    original_damage = super().cast(intelligence) # Method Overwriting- adds on functionality to an existing class
    # critical hit
    return original_damage * (float(random.randint(1, 10)) / 10 + 1)    # Not slicing- inclusive of 1 and 10
    
    
# Multiple Inheritance

import random

class Vest:
  def __init__(self, strength):
    self.damage_reduction = strength * 0.1
  
  def receive_damage(self, incoming_damage):
    
    if incoming_damage < self.damage_reduction:
      return 0
    else:
      return incoming_damage - self.damage_reduction

class Shield:
  def __init__(self, strength):
    self.damage_block_probability = 0.1
  
  def block_damage(self, incoming_damage):
    if random.random() <= self.damage_block_probability:
      print("BLOCKED!", end=' ')
      return 0
    else:
      return incoming_damage

class FireArmor(Shield, Vest):
  def __init__(self, strength):
    Shield.__init__(self, strength)
    Vest.__init__(self, strength)
  
  def receive_damage(self, incoming_damage, spell_type):
    damage_after_block = Shield.block_damage(self, incoming_damage)
    if spell_type == "FIRE":
      return Vest.receive_damage(self, damage_after_block) * 0.5 # Fire Armor reduces 50% damage from Fire Spells!
    else:
      return Vest.receive_damage(self, damage_after_block)
    
    
    
# has-a creates a class and is stored as an attribute of another class
# is-a is subclassing 

# Alias vs Deep Copy vs Shallow Copy

import copy
    
Jane = ("Jane", 10, 10, 10, "FIRE")
 
Jane_alias = Jane                   # aliasing
print(Jane is Jane_alias)           # true
 
Jane_deepcopy = copy.deepcopy(Jane) # deep copy
print(Jane is Jane_deepcopy)        # false

Jane_shallowcopy = copy.copy(Jane)
print(Jane is Jane_shallowcopy)
    
    
# Line    
class Line:
  def __init__(self, c0, c1):
    self.c0 = c0
    self.c1 = c1

  def __call__(self, x):
    return self.c0 + self.c1 * x

  def __str__(self):
    return f"{self.c0}, {self.c1}"   

y = Line(1 , 2)
print(y)
print(y(1))


# Quadratic 
class QuadraticLine(Line):
  def __init__(self, c0, c1, c2):       #function throws back inputs not used back to the parent class- Line
    super().__init__(c0 , c1)
    self.c2 = c2
  
  def __call__(self, x): 
    return super().__call__(x) + self.c2 * (x **2)

  def __str__(self):
    return f"{self.c0}, {self.c1}, {self.c2}" 

q = QuadraticLine(1 , 2 , 3)
print(q)
print(q(1))


# Cubic Line
class CubicLine(QuadraticLine):
  def __init__(self, c0, c1, c2, c3):    #function throws back inputs not used back to the parent class- QuadraticLine
    super().__init__(c0, c1, c2)
    self.c3 = c3
  
  def __call__(self, x): 
    return super().__call__(x) + self.c3 * (x **3)

  def __str__(self):
    return f"{self.c0}, {self.c1}, {self.c2}, {self.c3}" 
    
y = CubicLine(1, 2, 3, 4)
print(y)
print(y(1))

    
# W8 HW1

## Seniors' Method
class Time:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    
    @property
    def elapsed_time(self): #time getter
        return (self._hours*(3600) + self._minutes*60 + self._seconds)
    
    @elapsed_time.setter
    def elapsed_time(self, elapse): #time setter
            self._elapsed_time = elapse
            self._hours = self._elapsed_time // (3600) % 24
            self._minutes = self._elapsed_time // 60 % 60
            self._seconds = self._elapsed_time % 60
            return self.elapsed_time
    
    def __str__(self):
        return f"Time: {self._hours}:{self._minutes}:{self._seconds}"

## Recommended Method

class Time:
    
    def __init__(self,hours,minutes,seconds):
        self._hours = hours 
        self._minutes = minutes 
        self._seconds = seconds 
        
    def get_time(self):
        return (self._hours*(3600) + self._minutes*60 + self._seconds)
    
    def set_time(self,time):
        
        self._hours = time // (3600)
        self._hours %=  24
        self._minutes = (time % 3600) // 60
        self._hours %=  60
        self._seconds = ((time % 3600) % 60)
        self._seconds %= 60
        
    def __str__(self):
        return f"Time: {self._hours}:{self._minutes}:{self._seconds}"
        
    elapsed_time = property(get_time,set_time)
    

# W8 HW2
    
class Account:
    
    def  __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        self._balance -= amount
    
    def __str__(self):
        return f"{self._owner}, {self._account_number}, balance: {self._balance}"


# W8 HW3

        
class Diff:
    
    def __init__(self, function, h= 1e-4):
        self._function = function
        self._h = h
    
    def __call__(self, x):
        return (self._function(x + self._h) - self._function(x)) / self._h
    
# W8 HW4

from itertools import zip_longest

class Polynomial:
    
    def __init__(self,coeff):
        self.coeff = coeff
    
    def __add__(self, poly):
        return Polynomial([e1 + e2 for (e1, e2) in zip_longest(self.coeff, poly.coeff, fillvalue = 0)])
    
    def __sub__(self, poly):
        return Polynomial([e1 - e2 for (e1, e2) in zip_longest(self.coeff, poly.coeff, fillvalue = 0)])
    
    def __call__(self, x):
        result = 0
        power = 0
        for index in self.coeff:
            result += x ** power * index
            power += 1
        return result
            
    def __mul__(self, poly):
        if len(self.coeff) >= len(poly.coeff):
            product = []
            for i in range(len(self.coeff)):
                col_num = [0] * i
                for j in range(len(poly.coeff)):
                    col_num.append(self.coeff[j] * poly.coeff[i])
                product.append(col_num)
            out = Polynomial([0]) 
            
            for k in range(len(product)):
                out = out + Polynomial(product[k])
            return out
                
        if len(self.coeff) < len(poly.coeff):
            product = []
            for i in range(len(poly.coeff)):
                col_num = [0] * i
                for j in range(len(self.coeff)):
                    col_num.append(self.coeff[j] * poly.coeff[i])
                product.append(col_num)
            out = Polynomial([0]) 
            
            for k in range(len(product)):
                out = out + Polynomial(product[k])
            return out

    def differentiate(self):   # updates self.coeff but does not give an output
       outcome = []
       for i in range(1, len(self.coeff)):
            outcome.append(self.coeff[i]*i)
       self.coeff = outcome 

    def derivative(self):      # updates self.coeff and gives an output
       outcome = []
       for i in range(1, len(self.coeff)):
            outcome.append(self.coeff[i]*i)
            
       return Polynomial(outcome)
  































    
    
    
    
    
    
       

