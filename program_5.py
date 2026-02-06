#Hot Dog
#Samuel Renneke, 2/6/2026

type = input("Hot Dog or Chili Dog?: ")
if type == "Hot Dog":
    price = 3.5
elif type == "Chili Dog":
    price = 4.5

cheese = input("Cheese? Yes or No: ")
if cheese == "Yes":
    price = price + 0.5

peppers = input("Pepper? Yes or No: ")
if peppers == "Yes":
    price = price + 0.75

onions = input("Onion? Yes or No: ")
if onions == "Yes":
    price = price + 1

tax = price * 0.07

print("Subtotal = ", price)
print("Tax = ", tax)
print("Total = ", price + tax)
