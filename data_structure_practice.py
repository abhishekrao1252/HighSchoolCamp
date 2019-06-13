"""
title: data_structure_practice
author: Abhishek Rao
date: 2019-06-13 11:33
"""

for i in [89, 41, 73, 90]:
    print(i, end=" ")

print()
print("=" * 30)

for i in range(5, 15):
    print(i, end=" ")

for i in range(100, 201, 10):
    print(i, end=" ")

for i in range(80, 31, 8):
    print(i, end=" ")

print()
print("=" * 30)

for i in range(3):
    print("alright", end=" ")

integer = 10
while integer >= 1:
    print(integer, end="-")
    integer = integer - 1

need = int(input("enter an integer greater than 0"))
while need < 0:
    print(need, end="-")
    need = int(input("enter an integer greater than 0"))

