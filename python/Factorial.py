def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial =", result)