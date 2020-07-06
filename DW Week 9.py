# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:38:28 2020

@author: hobin
"""
"""
start() – COMMAND -  assigns the starting state based on the variable start_state 
step() – COMMAND-  takes in an input, calls get_next_values() to determine the state and the output, updates the state and returns the output 
transduce() – COMMAND - takes in a list of inputs and calls step() for each input in sequence 
get_next_values() - QUERY -  currently, it takes in the state and input and returns the same state and input. You override this by defining your own implementation in a child class. 

"""


# W9 C1

from libdw import sm

class CM(sm.SM): 
#define your starting state. 
    start_state = 0            
    
#this is your transition function. 
#You have to override it with your own definition 
    def get_next_values(self, state, inp):
        
        if (state == 0 and inp == 100):
            next_state = 0
            output = (0, "coke", 0)
        elif (state == 0 and inp == 50):
            next_state = 1
            output = (50, "--", 0)
        elif (state == 1 and inp == 50):
            next_state = 0
            output = (0, "coke", 0)
        elif (state == 1 and inp == 100):
            next_state = 0
            output = (0, "coke", 50)
        elif (state == 1 and (inp != 100 and inp != 50)):
            next_state = 1
            output = (50, "--", inp)
        elif (state == 0 and (inp != 100 and inp != 50)):
            next_state = 0
            output = (0, "--", inp)
            
        return next_state, output     

m = CM()
m.start()       # start the machine
print(m.state)  # see your state
print(m.step(50))  # give the state machine an input of 50
print(m.state)  # see your state
# m.state = 1  DO NOT WRITE THIS CODE, state is to be updated by step() only!

p = CM()
inputs_ls = [50, 50, 100, 50, 100, 50, 100]
p.transduce(inputs_ls, verbose = True)  # verbose does all the printing above


# W9 C2

from libdw import sm

class SimpleAccount(sm.SM):
    
    def __init__(self, start_value):
        self.start_state = start_value
    
    def get_next_values(self, state, inp):
        
        if state >= 100:
            next_state = state + inp
            output = next_state
            
        elif state < 100 and inp < 0:
            next_state = state + inp - 5
            output = next_state
        
        elif state< 100 and inp > 0:
            next_state = state + inp
            output = next_state
            
        return next_state, output
    

# Revision on different functions

class A:
    def __init__(self, i = 0):
        print('init')
        self.i = i
        
    def up(self):
        self.i += 1
        
    def __call__(self,i):
        print("call")
        
    def __eq__(self, i):
        print("ew")
        return False
    
    def __str__(self):
        print("str")
        return "cake"
    
a = A()
b = A(2)
a(1)
a == b
print(a)
    
    
# W9 H1

from libdw import sm

class CommentsSM(sm.SM):
    start_state = "string"

    def get_next_values(self, state, inp):
        
        if state == "string":
            if inp == "#":
                new_state = "comment"
                result = inp
            else:
                new_state = "string"
                result = None
                
        elif state == "comment":
            if inp == "\n":
                new_state = "string"
                result = None
            else:
                new_state = "comment"
                result = inp
       
        return new_state, result

# W9 H2
        
from libdw import sm

class FirstWordSM(sm.SM):
    start_state = "string"

    def get_next_values(self, state, inp):
        
        if state == "string":
            if inp == " " or inp == "\n":
                new_state = "string"
                result = None
            else:
                new_state = "comment"
                result = inp
                
                
        elif state == "blank":
            if inp == "\n":
                new_state = "string"
                result = None
            else: 
                new_state = "blank"
                result = None
                
                
        elif state == "comment":
            if inp == " ":
                new_state = "blank"
                result = None
            elif inp == "\n":
                new_state = "string"
                result = None
            else:
                new_state = "comment"
                result = inp

                    
        return new_state, result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
