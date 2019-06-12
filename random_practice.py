"""
title: random_practice
author: Abhishek Rao
date: 2019-06-12 09:53
"""

import random
name = input("enter your name here")
salary = int(input("enter your salary here"))
print(f"{name}, your current salary is {salary}")
raise_per = random.randint(1, 100)
raise_amount = salary + ((salary/100)*raise_per)
print(f"Your raise is {raise_per}% of {salary}")
print(f"{name}, your new salary is {raise_amount}")
