height = int(input("Enter your height: "))
bill = 0

if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 13
    
    photo = input("Do you want a photo? Y or N \n")
    if photo == "Y":
        bill += 3
    print(f"Your bill is ${bill}")
else:
    print("Can't ride")