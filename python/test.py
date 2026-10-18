# 1. Print the multiplication table of a number entered by the user.

# 2. Print the pattern:-

# *

# **

# ***

# ****

# *****

# 3. Remove duplicate values from a list while preserving the original order.

# 4. Find the largest and smallest values in a list without using max() or min()




#code 1

number = int(input("enter a num:"))

for i in range (1, 11):
    num = number * 1
    print(number, "x", i, "=", num)




#code 2

for i in range(1,6):
    print("*" * i)


#code 3

numbers = [3, 5, 3, 7, 5, 9, 7]

bob_numbers = []

for numbers in numbers:




#code 4

billy = [12, 7, 6, 5, 14, 15]

largest = billy[0]
smallest = billy[0]

for number in billy:
    if number > largest:
        largest = number


print("largest", largest)
print("smallest", smallest)