print("====================================")
print("        Welcome to BMI Checker       ")
print("====================================") 
print("Calculate your Body Mass Index (BMI)")
print("------------------------------------")

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2) 

# Determine BMI category
if bmi >= 25.0:
    category = "Overweight"
elif 18.5 <= bmi <= 24.9:
    category = "Healthy"
else:
    category = "Underweight"

# Display the results
print("------------------------------------")
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")
print("------------------------------------")
print("BMI Categories:")
print("Underweight: less than 18.5")
print("Healthy: 18.5 to 24.9")
print("Overweight: 25.0 or more")
print("====================================")