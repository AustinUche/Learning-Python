# Program that calculates the Body Mass Index (BMI) from a user's weight and height
print("Welcome to the BMI calculator")
height = float(input("Enter your height(m): "))
weight = int(input("Enter your weight(kg): "))
bmi = int(weight/height**2)
done = str(bmi)
print("Your Body Mass Index, BMI = " + done + " " + "kg/m^2")


