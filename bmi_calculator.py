weight = float(input("enter your weight (in kg)"))
height = float(input("enter your height(in meters)"))

bmi = weight / (height ** 2)
print(f"your BMI score is: {bmi:.2f}")
