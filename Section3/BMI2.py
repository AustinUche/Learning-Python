height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight: "))

BMI = round(weight / (height**2), 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI} kg/m^2 and it means you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI} kg/m^2 and it means you have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI} kg/m^2 and it means that you are overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI} kg/m^2 and it means that you are obese")
else:
    print(f"Your BMI is {BMI} kg/m^2 and it means you are clinically obese")