#functions
def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def division(a,b):
    return(a/b)

#input
print("CALCULTOR")
print("")
n1 = int(input("Enter your first number : "))
n2 = int(input("Enter your second number : "))
print("")
op = input("Enter which operator you want to use. \n '+' = addition, '-' = subtraction, \n '*' = multiplication, '/' = division : ")

#CALCULATOR PART
print("")
if op == '+':
    print("The sum is", add(n1,n2))
elif op == '-':
    print("The difference is", subtract(n1,n2))
elif op == '*':
    print("The product is", multiply(n1,n2))
elif op == '/':
    if n2 == 0:
        print("Denominator is zero")
    else:
            print("The quotient is", division(n1,n2))
else:
    print("Enter a valid operation")
