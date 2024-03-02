count = 0
for number in range(1, 101):
    count = number
    if number % 3 == 0 and number % 5 == 0:
        count = "FizzBuzz"        
    elif number % 5 == 0:
        count = "Buzz"
    elif number % 3 == 0:
        count = "Fizz"
    print(count)