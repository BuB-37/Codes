# CALCULATOR

#functions
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


#input
in1 = int(input("Enter the first number : "))
in2 = int(input("Enter the second number : "))
print("")

# input for type of operation
print("Press 1 for addition")
print("")
print("Press 2 for subtraction")
print("")
print("Press 3 for multiplication")
print("")
print("Press 4 for division")
print("")

op = input("Enter your choice of operation : ")
if op == '1':
    print("The sum is : ", add(in1,in2))
elif op == '2':
    print("The difference is : ", sub(in1,in2))
elif op == '3':
    print("The product is : ", multiply(in1,in2))
elif op == '4':
    print("The quotient is : ", divide(in1,in2))
else:
    print("Enter a valid number")