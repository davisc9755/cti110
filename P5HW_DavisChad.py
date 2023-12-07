# Creat a math quiz

# 11/29/23

# CTI-110 P5HW - Math Quiz

# Chad Davis

import random
random.randint(0, 100)

# Define a function to display the main menu

            

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

   
# Generate two random numbers between 1 and 100                       
def get_nums():
    """
function ask choose number and then
choose and dislpay two random numbers
    """
    num1 = random.randint(50, 100)
    num2 = random.randint(0, 49)
    return num1, num2

# Adds and  Calculate the correct answer

def addCompare_nums(num1,num2):
    """
function ask to enter answers then check answer
if answer is correct returns congratultions  
    """
    answer = num1 + num2

    return answer
#Subtract and Calculate the correct answer

def subCompare_nums(num1, num2) :
    """
function ask to enter answers then check answer
if answer is correct returns congratulations
    """

    answer = num1 - num2

    return answer

# Main program    

import P5HW_DavisChad as fn
def main():

    choice = 0
# Loop until the user chooses to exit
    while choice !=3:

        fn.dis_menu()
        
        choice = int(input("Please choose one of the menu options:"))

        if choice == 1:
        
            n1, n2 = fn.get_nums()
            print(f' {n1}\n+{n2} ')
            answer = fn.addCompare_nums(n1, n2)
            guesses = 0
            user_answer = int(input("Enter answer.\n"))
            guesses += 1
                
            if user_answer == answer:
             print("Congratulations!!!! Your answer is correct.")
            elif user_answer < answer:
             user_answer = int(input("Try again:  \nSorry, guess to low. "))
             guesses += 1
             if user_answer == answer :
              print("Congratulations!!!! Your answer is correct.")
             elif user_answer > answer:
              user_answer = int(input("Try again:  \nSorry, guess to high. "))
              guesses += 1
             if user_answer == answer :
              print("Congratulations!!!! Your answer is correct.")
              print(f"Number of guesses: {guesses}")
        
        

        elif choice == 2:

              n1, n2  = fn.get_nums()
              print(f' {n1}\n-{n2} ')
              answer = fn.subCompare_nums(n1, n2)
              guesses = 0
              user_answer = int(input("Enter answer. \n"))
              guesses += 1

              if user_answer == answer:
               print("Congratulations!!!! Your answer is correct.")
              elif user_answer < answer:
               user_answer = int(input("Try again: \nSorry, guess is too low. "))
               guesses += 1
               if user_answer == answer:
                print("Congratulations!!!! Your answer is correct.")
               elif user_answer > answer:
                user_answer =int(input("Try again: \nSorry, guess is to high. "))
                guesses += 1
               if user_answer == answer:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                
        elif choice == 3:
           print("Thank you for playing...\nBye!!")

        else:
            print("Invald entry!!!")
            
            

            
                
            

main()


