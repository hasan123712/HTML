snack   = "Hershys"
price        = 2.00
quantity     = 50         
available = True
print("Snack:", snack)
print("Price: $", price)
print("In Stock:", quantity)
print("Available?", available)
print(type(snack))
print(type(price))
print(type(quantity))
print(type(available))
total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.5)
print("Double stock:", quantity * 3)
print("Is price under $3?", price < 3)
print("More than 20 in stock?", quantity > 20)
print("Is price exactly $1.50?", price == 2.00)
shop_name = "Meltin" + " " + "Bliss"
print("Shop name:", shop_name)
print("Letters in snack name:", len(snack))
print("First letter:", snack[0])
price_a = 2.00
price_b = 4.00
print("Before:", price_a, "and", price_b)
temp    = price_a
price_a = price_b
price_b = temp
print("After:", price_a, "and", price_b)