"""
title: string_practice
author: Abhishek Rao
date: 2019-06-11 13:46
"""
import random

short_hand = "Thank you for that! You are too sweet and kind"
short_hand = short_hand.replace("Thank", "Thnk")
short_hand = short_hand.replace("you", "U")
short_hand = short_hand.replace("for", "4")
short_hand = short_hand.replace("that", "tht")
short_hand = short_hand.replace("You", "U")
short_hand = short_hand.replace("are", "r")
short_hand = short_hand.replace("too", "2")
short_hand = short_hand.replace("sweet", "swt")
short_hand = short_hand.replace("and", "&")
short_hand = short_hand.replace("kind", "knd")
print(short_hand)
# this is the short hand activity which basically just used the replace function a bunch

phrase = "Madam, I'm Adam"
phrase = phrase.replace("Madam, ", "madam")
phrase = phrase.replace("I'm", "im")
phrase = phrase.replace(" Adam", "adam")
print(phrase)


first_name = input("enter your first name")
last_name = input("enter your last name/surname")
home = input("enter the city you were born")
university = input("enter the university you graduated from")
relative_name = input("enter a name of a relative")
friend_name = input("enter a name of a friend")
label1 = "Employee ID"
Label2 = "User Name"
Label3 = "Password"

def employee_id (first_name,  last_name, home, university, relative_name, friend_name):
    (first_name[:4]) + (last_name[:-2]) + "\n"
    (home[:3]) + (university[:-4]) + "\n"
    char_num = len(relative_name)
    start = random.randint(0, char_num)
    print(relative_name[start:])
    num_of_char = len(friend_name)
    end = random.randint(0, num_of_char)
    return print(friend_name[:end])


































































