#Program to check who can buy a ticket

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    elif age >= 45 and age <= 55:
        print("You do not have to pay any bill")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller to ride the rollercoaster.")