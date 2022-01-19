# For Loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print("\n")


# range() function
# for number in range(a, b):
#    print(number)

# # usefull for do something to a range of something
# # For Loop with Range
# for number in range(1, 10):  # 1 thru 10, not including 10
#     print(number)

# # first number one is starting point, second number is ending point, and third number is the step, so 3 means every third
# for number in range(1, 11, 3):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
