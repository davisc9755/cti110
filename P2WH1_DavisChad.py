# travel expense program II

# 10/09/2023

# CTI-110 P2HW1 - Travel

# Chad Davis

# Budget and destination info

user_budget = float(input('Enter Budget:'))

user_destination = input('Enter travel destination:')

# Expense info

user_gas = float(input('How much do you think you will spend on gas:'))

user_accommodations = float(input('How much will you need for a hotel:' ))

user_food = float(input('How much you need for food:'))

# add expense

total_expense = user_gas + user_accommodations + user_food

# subtract expense from budget

remaining_balance = user_budget - total_expense
# Travel Expenses output

print("------------Travel Expenses------------")

print(f'{"Location:"}           {user_destination:}')

print(f'{"Initial Budget:"}     ${user_budget:.1f}')

print(f'{"Fuel:"}               ${user_gas:.1f}')

print(f'{"Accomodation:"}       ${user_accommodations:.1f}')

print(f'{"Food:"}               ${user_food:.1f}')

print("----------------------------------------")

print(f'{"Remaining Balance:"}  ${remaining_balance:.1f}')

