# Creat a math quiz

# 11/29/23

# CTI-110 P5HW - Math Quiz

# Chad Davis

import random
random.randint(0, 100)


def dis_menu():
    """
    display list of options
    """

    print("Welcome to Math Quiz")
    print("\n")
    print("MAIN MENU")
    print("----------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit \n")
    
    
def get_nums():
    """
function ask choose number and then
choose and dislpay two random numbers
    """
    num1 = random.randint(50, 100)
    num2 = random.randint(0, 49)
    return num1, num2

def addCompare_nums(num1,num2):
    """
function ask to enter answers then check answer
if answer is correct returns congraualtion if 
    """
    answer = num1 + num2

    return answer

def subCompare_nums(num1, num2) :

    answer = num1 - num2

    return answer
                   
      



    
        
        
        
    
    

     
