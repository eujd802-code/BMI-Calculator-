#BMI Calculator Version 1

weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))

def questions(weight, height):

    bmi = (weight * 703) / (height ** 2)
    if bmi < 18.5:
        print("underweight")
    elif bmi > 18.5 and bmi < 25:
        print("normal")
    elif bmi > 25 and bmi < 30:
        print("overweight")
    elif bmi > 30:
        print("obese")
    print(f"Your BMI is: {bmi:.2f}")

questions(weight, height)
