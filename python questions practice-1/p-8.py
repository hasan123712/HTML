price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount = price * discount_percentage / 100
final_price = price - discount

print("Discount amount: $", discount)
print("Final price: $", final_price)