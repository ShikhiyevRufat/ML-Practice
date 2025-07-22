# Bir şirkətdə işçilərin maaşlarını idarə edən bir sistem yaratmalısınız.

import numpy as np


employees = []
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"{self.name} age is {self.age} and salary is {self.salary}")

for i in range(3):
    name = input("Name:")
    age = int(input("Age:"))
    salary = int(input("Salary:"))

    employee = Employee(name, age, salary)
    employee.display_info()
    employees.append([name,age, salary])

get_salary = [row[2] for row in employees]
salary_percent = lambda a: (a*20)/100
result_map = list(map(salary_percent, get_salary))
print(result_map)

print("-"*100)
get_ages= [row[1] for row in employees]
age_great = lambda a: a>30
result_filter = list(filter(age_great, get_ages))
print(result_filter)

print("-"*100)
avarage_of_salary = np.mean(get_salary)
print(avarage_of_salary)