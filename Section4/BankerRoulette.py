import random
#Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names =names_string.split(",")
length = len(names)
random_choice = random.randint(0, length - 1)
person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} is going to pay the bills")
