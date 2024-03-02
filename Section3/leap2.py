year = int(input("Which year do you want to check? "))         
first = year % 4
second = year % 100
third = year % 400
if first == 0:
    if second == 0:
        if third == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")