"""
Created on Apr 2020

@author: hobingxuan (1004131)

Video Link: https://youtu.be/mQ_D4Ri9dCA

"""

import libdw.sm as sm
import time
import sys
import random
import operator

class MathGame(sm.SM):

    def __init__(self):
        self.start_state = 'START'
        print("\nWelcome to the Math Challenge Game created during E- Learning!\n")
        time.sleep(0.5)
        print("Are you ready for the challenge?")
        time.sleep(0.5)

    def get_next_values(self, state, inp):
        if state == "START":
            if inp == "a" or inp == "A":
                print("\nGame starting... ")
                time.sleep(0.25)
                user_score = 0
                next_state = "GAME"
                
            elif inp != "a" or inp != "A":
                print("\nPlease give a valid input.\n")
                user_score = 0
                next_state = state
            
        elif state == "GAME":
            try:    #try tests the following code and the except block handles the error from rounding an invalid string input
                print("\nWhat Level do you want to challenge? (Easy/ Medium/ Hard)\n")
                user_input = input("Level Choice: ")
                if user_input == "Easy" or user_input == "easy" or user_input == "EASY":
                    print("\nLoading Easy Questions... ")
                    user_score = 0
                    next_state = "GAMING"
                
                elif user_input == "Medium" or user_input == "medium" or user_input == "MEDIUM":
                    print("\nLoading Medium Level Questions... ")
                    user_score = 0
                    next_state = "MEDIUM GAMING"
                
                elif user_input == "Hard" or user_input == "hard" or user_input == "HARD":
                    print("\nLoading Hard Questions... ")
                    user_score = 0
                    next_state = "HARD GAMING"
                    
                else:
                    user_input_str = str(user_input)
                    print("\nPlease choose a valid level")
                    user_score = 0
                    next_state = state
            except:
                print("\nPlease choose a valid level")
                user_score = 0
                next_state = state

            
        elif state == "GAMING":
            user_score = 0
            for index in range(5):
                try:    #try tests the following code and the except block handles the error from rounding an invalid string input
                    question_input = round(self.math_qn_easy(), 2)
                    user_input = float(input("What is your answer? "))
                    rounded_input = round(user_input,2)
                    if rounded_input == round(question_input, 2):
                        user_score += 20
                        print("Keep up the good work!")
                        print(f"Your current score is: {user_score} / 100 \n")
                        time.sleep(0.15)
    
                    else:
                        print("Wrong answer! Practice more!")
                        print(f"Your current score is: {user_score} / 100 \n")
                        time.sleep(0.15)
                except:
                    print("Please input only integers or floats.")
            

            print(f'Your final score is {user_score} / 100')
            print("Do you want to challenge the next level? (Y/N)")
            check = input("Choice: ")
            if check.upper() == "Y":
                user_score = 0
                next_state = "GAME"
            else:
                if user_score <= 50:
                    print("\nWinners never quit. Your score was 50 and below. \nThe game will be restarted for you automatically.\nYou are welcome.")
                    user_score = 0
                    next_state = "START"                 
                else:
                    print("\nMath Game will be closed. Goodbye.\n")
                    sys.exit()
                    
        elif state == "MEDIUM GAMING":
            user_score = 0
            for index in range(10):
                try:    #try tests the following code and the except block handles the error from rounding an invalid string input
                    question_input = round(self.math_qn_medium(), 2)
                    user_input = float(input("What is your answer? "))
                    rounded_input = round(user_input,2)
                    if rounded_input == round(question_input, 2):
                        user_score += 10
                        print("Keep up the good work!")
                        print(f"Your current score is: {user_score} / 100 \n")
                        time.sleep(0.15)
    
                    else:
                        print("Wrong answer! Practice more!")
                        print(f"Your current score is: {user_score} / 100 \n")
                        time.sleep(0.15)
                except:
                    print("Please input only integers or floats.")
            

            print(f"Your final score is {user_score} / 100\n")
            print("Do you want to challenge the next level? (Y/N)")
            check = input("Choice: ")
            if check.upper() == "Y":
                user_score = 0
                next_state = "GAME"
            else:
                if user_score <= 50:
                    print("\nWinners never quit. Your score was 50 and below. \nThe game will be restarted for you automatically.\nYou are welcome.")
                    user_score = 0
                    next_state = "START"                 
                else:
                    print("\nMath Game will be closed. Goodbye.\n")
                    sys.exit()
            
        elif state == "HARD GAMING":
            user_score = 0
            for index in range(10):
                try:    #try tests the following code and the except block handles the error from rounding an invalid string input
                    question_input = round(self.math_qn_hard(), 2)
                    user_input = float(input("What is your answer? "))
                    rounded_input = round(user_input,2)
                    if rounded_input == round(question_input, 2):
                        user_score += 10
                        print("Keep up the good work!")
                        print(f"Your current score is: {user_score} / 100 \n")
                        time.sleep(0.15)
    
                    else:
                        print("Wrong answer! Practice more!")
                        print(f"Your current score is: {user_score} / 100 \n")
                        time.sleep(0.15)
                except:
                    print("Please input only integers or floats.")
            

            print(f"Your final score is {user_score} / 100\n")
            print("Do you want to break your high score and try again? (Y/N)\n")
            check = input("Choice: ")
            if check.upper() == "Y":
                user_score = 0
                next_state = "GAME"
            else:
                if user_score <= 50:
                    print("\nWinners never quit. Your score was 50 and below. \nThe game will be restarted for you automatically.\nYou are welcome.")
                    user_score = 0
                    next_state = "START"                 
                else:
                    print("\nMath Game will be closed. Goodbye.\n")
                    sys.exit()
       
        return next_state, user_score
            

    def math_qn_easy(self):
        signs = {'x': operator.mul, '/': operator.truediv, '+': operator.add, '-': operator.sub}
        first_number = random.randint(10, 20)
        second_number = random.randint(1, 10)

        problem = random.choice(list(signs.keys()))
        question = signs.get(problem)(first_number, second_number)   #If the key exists in the {signs}, then value for that key is returned
        print(f'\nWhat is the answer to {first_number} {problem} {second_number}? Round to 2dp if applicable')
        return question
    
    def math_qn_medium(self):
        signs = {'x': operator.mul, '/': operator.truediv, '+': operator.add, '-': operator.sub}
        first_number = random.randint(10, 100)
        second_number = random.randint(10, 100)
    
        problem = random.choice(list(signs.keys()))
        question = signs.get(problem)(first_number, second_number)   #If the key exists in the {signs}, then value for that key is returned
        print(f'\nWhat is the answer to {first_number} {problem} {second_number}? Round to 2dp if applicable')
        return question
    
    def math_qn_hard(self):
        signs = {'x': operator.mul, '/': operator.truediv, '+': operator.add, '-': operator.sub}
        first_number = random.randint(100, 1000000)
        second_number = random.randint(10, 1000)

        problem = random.choice(list(signs.keys()))
        question = signs.get(problem)(first_number, second_number)   #If the key exists in the {signs}, then value for that key is returned
        print(f'\nWhat is the answer to {first_number} {problem} {second_number}? Round to 2dp if applicable')
        return question

    

game = MathGame()
game.start()
while True:
    user_input = input("\nPress 'A' to continue: ")
    game.step(user_input)

