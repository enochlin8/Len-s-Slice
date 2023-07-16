# Your code below:

# Checkpoint 1, Keeping track of what Pizza toppings we have.
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Checkpoint 2, Keeping track of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Checkpoint 3, Counting how many occurences of 2s in the price list.
num_two_dollar_slices = prices.count(2)

#Checkpoint 4, Finding the length of the toppings
num_pizzas = (len(toppings))

#Checkpoint 5, Printing this statement
print("We sell "  +str (num_pizzas) + " different kinds of pizza!")

#Checkpoint 6, Creating  a two dimensional list.
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

#Checkpoint 7, Sorting the two dimensional list.
pizza_and_prices.sort()

#Checkpoint 8, Storing element into the new variable.
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
#Checkpoint 9, Getting the most expensive pizza from the list.
priciest_pizza =pizza_and_prices[6]

#Checkpoint 10, Removing the most expensive pizza because it was our last one.
pizza_and_prices.pop(6)

#Checkpoint 11, Adding peppers as a new topping.

pizza_and_prices.insert(3, "peppers")

#Checkpoint 12, Slicing the list for the 3 lowest costing pizza.
three_cheapest = pizza_and_prices[:3]

#Checkpoint 13, Printing the list.
print(three_cheapest)