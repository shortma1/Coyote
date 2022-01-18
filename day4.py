# random module needed to use random functionality
import random

# created my_module.py file in same folder, created variable pi and referenced it in print my_module.pi
import my_module
print(my_module.pi)

# randint gives a random integer between the two numbers given including the two numbers.
random_integer = random.randint(1, 10)
print(f"Random Integer = {random_integer}")

# random.random give two numbers between 0 and 1.0 not including those two numbers
random_float = random.random()
print(f"Random Float = {random_float}")

# get a decimal number between 0 and 5, use the above random_float and multiply it by 5
onetofive = random_float * 5
print(f"The number is ={onetofive}")

# List
fruits = ["apple", "pear", "banana"]
print(fruits[0])  # prints apple
print(fruits[-1])  # prints last item in list
fruits[1] = "cherry"  # change a variable
print(fruits[1])

fruits.append("pear")  # to add to the end of a list
print(fruits)
# https://docs.python.org/3/tutorial/datastructures.html  for more information on list

""" # Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_names = len(names)
print(names)
print(num_names)
random_integer = random.randint(0, num_names - 1) # -1 because list starts with 0, list length is 1 more because is counts 0 as 1
print(random_integer)
print(f"{names[random_integer]}, you are paying for supper!")
 """
