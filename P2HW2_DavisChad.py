
# CTI-110

# P2HW2-List

# Chad Davis

# 10/09/2023

# Test Grades List

Module_1 = float(input('Enter grade for Module 1:'))

Module_2 = float(input('Enter grade for Module 2:'))

Module_3 = float(input('Enter grade for Module 3:'))

Module_4 = float(input('Enter grade for Module 4:'))

Module_5 = float(input('Enter grade for Module 5:'))

Module_6 = float(input('Enter grade for Module 6:'))

lowest_grade = min(Module_1, Module_2, Module_3, Module_4, Module_5, Module_6)

highest_grade = max(Module_1, Module_2, Module_3, Module_4, Module_5, Module_6)

grade_total = (Module_1 + Module_2 + Module_3 + Module_4 + Module_5 + Module_6)

grade_average = ( grade_total / 6)

# Results

print("------------Resutls------------")

print(f'{"Lowest Grade":}     {lowest_grade:.1f}')

print(f'{"Highest Grade":}    {highest_grade:.1f}')

print(f'{"Sum of Grade":}     {grade_total:.1f}')

print(f'{"Average":}          {grade_average:.2f}')

print("--------------------------------")



