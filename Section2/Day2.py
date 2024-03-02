print("Welcome to the tip calculator!!")
bill = int(input("What is the total bill?\n"))
percentage_tip = int(input("What percentage tip would like to give?\n"))
persons = int(input("How many people are to split the bill? "))

bill_plus_tip = (bill) + (percentage_tip / 100)
bill_per_person = round((bill_plus_tip / persons), 2)

print(f"Each person would have to pay a bill of ${bill_per_person}")
