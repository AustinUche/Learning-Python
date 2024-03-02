#Program to calculate the number of days, weeks and months remaining for a person to live assuming the person had a total of 90 years to live

month = 30 #number of days in a month
week = 7 #number of days in a week
year = 365 #number of days in a year
ninety_years = 365*90 #number of days in 90 years - 32850 days

current_age = int(input("Input your current age: "))

num_days_left = int(ninety_years - (current_age * year)) #total days in 90 years - total days lived in current age
num_weeks_left = int((((year//week)*ninety_years)//year) - ((year//week)*(current_age*year))//year) #total weeks in 90 years - total weeks lived in current age
num_months_left = int((((year//month)*ninety_years)//year) - ((year//month)*(current_age*year))//year) #total months in 90 years - total months lived in current age

print(f"You have {num_days_left} days, {num_weeks_left} weeks and {num_months_left} months left. ")


#############OR########################## 

age = input("What is your current age? ")
age_as_int = int(age) #converting the variable age input to an int

years_remaining = 90 - age_as_int #total years to live - current age
weeks_remaining = years_remaining * 52 # remaining years to live * number of weeks in a year
months_remaining = years_remaining * 12 # remaining years to live * number of months in a year
days_remaining = years_remaining * 365 # reamining years to live * number of days in a year

print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months remaining")