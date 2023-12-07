# CTI-110

# P3HW2 - Salary

# Chad Davis

# 10/16/2023

# Employee pay calculation

# get employee's info

employee_name = input("Enter employee's name:")

hours_worked = float(input("Enter number of hours worked:"))

pay_rate = float(input("Enter employee's pay rate:"))

# dislpay results

print("---------------------------------------")

print(f'{"Employee name:"}  {employee_name:}\n')

print(f'{"Hours Worked"}   {"Pay Rate"}    {"Overtime"}    {"OverTime Pay"}    {"RegHour Pay"}     {"Gross Pay"}')

print("--------------------------------------------------------------------------------")

# evalute if the employe did overtime

if hours_worked > 40 : # they did overtime

    #calculate how much they get paid for overtime hours
    hours_worked = 40
    over_hours = 5
    total_hours = hours_worked 

    over_pay = pay_rate * 1.5 * over_hours

    reg_pay = pay_rate * hours_worked

    gross_pay = pay_rate * 40 + over_pay

else:
    gross_pay = hours_worked + over_pay

print(f'{total_hours:<15.1f}{pay_rate:4.1f}{over_hours:11.1f}{over_pay:15.2f}{reg_pay:16.2f}{gross_pay:16.2f}')
    
