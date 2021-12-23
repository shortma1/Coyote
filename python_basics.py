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
num = int(input("Is this an odd number? "))
if num % 2 == 0:
    print("No that was not an odd number.")
else:
    print("Yes that was an odd number.")
