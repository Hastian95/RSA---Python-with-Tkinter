#1. Cory Shafer yt1:
#https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2025,2,10)

print(Employee.is_workday(my_date))

emp_1 = Employee('Pawel','Ka',7000)
emp_2 = Employee('Jon','Mike',5800)

#print(emp_2.fullname())
#print(Employee.fullname(emp_1))

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
#print(Employee.num_of_emps)

#Employee.raise_amount = 1.06    #to samo co poniżej
#Employee.set_raise_amt(1.05)    #to samo = tylko tutaj używamy classmethod

#emp_str_1 = 'John-Doe-6000'
#emp_str_2 = 'Steve-Navish-3400'
#emp_str_3 = 'Jessica-Towns-8700'
#new_emp_1 = Employee.from_string(emp_str_1)
#print(new_emp_1.email, new_emp_1.pay)
#print(Employee.num_of_emps)

