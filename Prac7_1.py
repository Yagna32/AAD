import pandas as pd
import matplotlib.pyplot as plt


def binarySearch(YGN,num,count=0):
    mid  = len(YGN)//2
    
    count += 1
    if (mid == 0 or mid == len(YGN)-1) and not(YGN[mid] == num):
        return count
    if num == YGN[mid]:
        return count
    elif num < YGN[mid]:
        return binarySearch(YGN[:mid],num,count)
    else :
        return binarySearch(YGN[mid:],num,count)
    
def linearSearch(YGN,num):
    count = 0

    for i in range(0,len(YGN)):
        count += 1
        if num == YGN[i]:
            return count
    
    return -1

data = pd.read_csv('Prac7_data.csv')
print(data)
salary = list(data['Salary'])
max_salary = max(salary)
Max_sal_lincount = linearSearch(salary,max_salary)
Max_sal_bicount = binarySearch(salary,max_salary)

designation = list(data.loc[data['Salary']==max_salary]['designation'])
print('Designation of Employee with most salary\n')
print(f'\tMaximum Salary: {max_salary}')
print(f'\tDesignation: {designation}')
print(f'\tLinear Search Count: {Max_sal_lincount}')
print(f'\tBinary Search Count: {Max_sal_bicount}')
print()

Min_salary = min(salary)
Min_sal_lincount1 = linearSearch(salary,Min_salary)
Min_sal_bicount1 = binarySearch(salary,Min_salary)

Name = list(data.loc[data['Salary']==Min_salary]['Name'])
print('Name of the Employee with least salary\n')
print(f'\tMinimum Salary: {Min_salary}')
print(f'\tName of Employee: {Name}')
print(f'\tLinear Search Count: {Min_sal_lincount1}')
print(f'\tBinary Search Count: {Min_sal_bicount1}')
print()

Age = list(data['Age'])
Min_age = min(Age)
Min_age_lincount = linearSearch(Age,Min_age)
Min_age_bicount = binarySearch(Age,Min_age)

Mobile_num = list(data.loc[data['Age']==Min_age]['Mobile-number'])
print('Mobile number of youngest employee\n')
print(f'\tMinimum Age: {Min_age}')
print(f'\tMobile Number of Employee: {Mobile_num}')
print(f'\tLinear Search Count: {Min_age_lincount}')
print(f'\tBinary Search Count: {Min_age_bicount}')
print()


Max_age = max(Age)
Max_age_lincount = linearSearch(Age,Max_age)
Max_age_bicount = binarySearch(Age,Max_age)

Oldest_salary = list(data.loc[data['Age']==Max_age]['Salary'])

print('Salary of the Oldest Employee\n')
print(f'\tMaximum Age: {Max_age}')
print(f'\tSalary of Employee: {Oldest_salary}')
print(f'\tLinear Search Count: {Max_age_lincount}')
print(f'\tBinary Search Count: {Max_age_bicount}')
print()
