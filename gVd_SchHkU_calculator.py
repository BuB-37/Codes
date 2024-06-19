# Functions 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

# Main program
print("CALCULATOR")
print("")

while True:
    # Input numbers
    n1 = int(input("Enter your first number: "))
    n2 = int(input("Enter your second number: "))
    print("")

# Calculator
    op = input("Enter which operator you want to use.\n'+' = addition, '-' = subtraction,\n'*' = multiplication, '/' = division: ")
    print("")

    # Calculator part
    if op == '+':
        print("The sum is", add(n1, n2))
    elif op == '-':
        print("The difference is", subtract(n1, n2))
    elif op == '*':
        print("The product is", multiply(n1, n2))
    elif op == '/':
        if n2 == 0:
            print("Denominator is zero, division by zero is not allowed")
        else:
            print("The quotient is", division(n1, n2))
    else:
        print("Enter a valid operation")

    # Ask user if they want to continue or stop
    print("")
    continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("")
        print("Thank you for using the calculator. Goodbye!")
        break
    print("")
