import math

def calculate(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a* b) // gcd
    return lcm

num1 = int(input("Enter the first number for the LCM : "))
num2 = int(input("Enter the second number for the LCM : "))
result = calculate(num1, num2)
print('The LCM of', num1,'and', num2,'is : ',result) 