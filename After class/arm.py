# 1. USER INPUT: Get the number as a string to count digits easily
num_str = input("Enter a positive number: ")

# Find the order 'n' (number of digits)
n = len(num_str)

# Convert string input to integer for final comparison
original_num = int(num_str)

sum_of_powers = 0

# 2. LOOP: Iterate through each digit in the input
for digit_char in num_str:
    digit = int(digit_char)
    sum_of_powers += digit ** n  # Raise digit to power 'n' and add to sum

# 3. CONDITIONAL STATEMENT: Compare calculated sum to original number
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong Number!")
else:
    print(f"{original_num} is NOT an Armstrong Number.")