# travel expense program

# 09/27/2023

# CTI-110 P1HW2 - Travel Expense

# Chad Davis

# Budget and destination info

user_budget = int(input('Enter Budget:'))

user_destination = input('Enter travel destination:')

# Expense info

user_gas = int(input('How much do you think you will spend on gas:'))

user_accommodations = int(input('How much will you need for a hotel:' ))

user_food = int(input('How much you need for food:'))

# add expense

total_expense = user_gas + user_accommodations + user_food

# subtract expense from budget

remaining_balance = user_budget - total_expense

print( 'Remaining Balance:',  remaining_balance)

