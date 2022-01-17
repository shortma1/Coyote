# Practice Python File

#from pathlib import Path
# print(Path.home())

# print("Hello!")

#message = input("Type your message there: ")
# print(message)
# length = len(message)  # len() gets the length of a string
# print(length)

# numint = int(3.14)  # int() changes float num to int
# print(numint)

# numfloat = float(3)
# print(numfloat)

# print(type(3.14))  # type() tells you what type it is.

# print(str(numfloat))  # str() converts varible to string type

# Note - to comment out highlited code on Mac - cmd + /

# 3 + 5  # addition
# 7 - 4  # subtraction
# 3 * 2  # multiplicaton
# 6 / 3  # division, note product is always a float
# 2 ** 2  # power ie 2 to the power of 2
# print(2 ** 2)

# PEMDASLR order of operation
# ()
# **
# * /
# + -
# print(3 * 3 + 3 / 3 - 3)

# round() rounds numbers to specified amount ,2 specifies round to two decimal places
# print(round(8 / 3))
# print(round(8 / 3, 2))

# // is the floor division operator, it causes the division to round down.
# print(8 // 3)

# score = 0
# score += 10  # adds one
# score -= 1  # sutracts one
# score *= 2  # multipy
# score /= 2  # division

# print(f"your score is {score}.")  # f-string

# if conditional
# height = 119
# if height >= 120:
#     print("You can ride!")
# else:
#     print("You can not ride!")

# # Comparison operators
# > Greater than
# < Less than
# >= greater than or equal 2
# <= less than or equal 2
# == equal to

# % modulo will give you the remainer of a value
# num = int(input("Is this an odd number? "))
# if num % 2 == 0:
#     print("No that was not an odd number.")
# else:
#     print("Yes that was an odd number.")

# elif if conditions
# if condition:
#     do a
# elif condtion:
#     do b
# else:
#     do c

# nested if conditions
# if condition:
#     if condition:
#         do a
#     else:
#         do b
# else:
#     do c

# if / elif / else
# if condition1:
#    do A
# elif condition2:
#    do B
# else:
#    do C

# Logical Operators
# A and B must be True
# C or D just one must be true
# not E not true

# if condition1 & condition2 & condition3:

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

true = 0
love = 0

true += name1_lower.count("t")
true += name1_lower.count("r")
true += name1_lower.count("u")
true += name1_lower.count("e")
true += name2_lower.count("t")
true += name2_lower.count("r")
true += name2_lower.count("u")
true += name2_lower.count("e")

love += name1_lower.count("l")
love += name1_lower.count("o")
love += name1_lower.count("v")
love += name1_lower.count("e")
love += name2_lower.count("l")
love += name2_lower.count("o")
love += name2_lower.count("v")
love += name2_lower.count("e")
lovenum = str(true) + str(love)
lnum = int(lovenum)
if (lnum <= 10) or (lnum >= 90):
    print(f"\nYour score is {lnum}, you go together like coke and mentos.")
elif (lnum >= 40) or (lnum <= 50):
    print(f"\nYour score is {lnum}, you are alright together.")
else:
    print(f"\nYour score is: {lnum}.")
