pizza = ("Cheese pizza", 30, "Italian")
pasta = ("Alfredo Pasta", 25, "Italian")
pizza_ingredients = {"flour", "cheese", "tomato",}
pasta_ingredients = {"pasta", "cheese", "tomato", "chicken"}
print("Recipe 1:", pizza[1])
print("Recipe 2:", pasta[1])
print("All ingredients:", pizza_ingredients | pasta_ingredients)
print("Common ingredients:", pizza_ingredients & pasta_ingredients)
print("Only Pizza:", pizza_ingredients - pasta_ingredients)
print("Only Pasta:", pasta_ingredients - pizza_ingredients)
print("Special ingredients:", pizza_ingredients ^ pasta_ingredients)