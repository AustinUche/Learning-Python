#Program for Pizza delivery
print("Welcome to Python Pizza Delivery!")
bill = 0
size = input("What size of pizza do you want? S, M or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# S = 15
# M = 20
# L = 25
pepperoni_small_pizza = 2
pepperoni_medium_large_pizza = 3
extra_cheese_pizza = 1

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += pepperoni_small_pizza
        if extra_cheese == "Y":
            bill += extra_cheese_pizza
            print(f"Your total bill is ${bill}")
        else: 
            print(f"Your total bill is ${bill}")
    else:
        if extra_cheese == "Y":
            bill += extra_cheese_pizza
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large_pizza
        if extra_cheese == "Y":
            bill += extra_cheese_pizza
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
    else:
        if extra_cheese == "Y":
            bill += extra_cheese_pizza
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large_pizza
        if extra_cheese == "Y":
            bill += extra_cheese_pizza
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
    else:
        if extra_cheese == "Y":
            bill += extra_cheese_pizza
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
