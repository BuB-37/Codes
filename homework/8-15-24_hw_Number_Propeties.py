def check_number_properties(number):
    """Check and print the properties of the number."""
    if number <= 1:
        print("Neither prime nor composite")
    elif number == 2:
        print("Even") 
        print("Prime")
    elif number % 2 == 0:
        print("Even")
        print("Composite")
    else:
        print("Odd")
        is_prime = True
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
                break
        print("Prime" if is_prime else "Composite")

# Input from the user
number = int(input("Enter a number: "))

# Print the properties
print("------------------")
check_number_properties(number)
print("------------------")