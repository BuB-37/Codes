
print("IS IT A PERFECT SQAURE ROOT CALCULATER")
print('')

def square(root): 
    num = 1
    while num * num <= root:
        if num * num == root:
            return True 
        num += 1
    return False

input_square = int(input("Enter your number to see if it is a perfect square root : "))
print('')
print("If it says 'True' this means it is a perfect square root.")
print('')
print("If it says 'False this means it is not a perfect square root'")
print('')

print(square(input_square))



