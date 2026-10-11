# Input example
weight = 50 # kg
height = 180 # cm

bmi = weight / ((height / 100) ** 2)
print(f"Height: {height} cm") # f is used to format the string with variables
print(f"Weight: {weight} kg")
print("BMI Calculation:")
print(f"BMI: {bmi:.2f}")
print("BMI 18.5-24.9: Normal weight")
if bmi < 18.5:
    print("BMI < 18.5: Unhealthy weight")