#asking for input
n1 = int(input("Enter your first number : "))
n2 = int(input("Enter your second number : "))
n3 = int(input("Enter your third number : "))
n4 = int(input("Enter your fourth number : "))
n5 = int(input("Enter your fifth number : "))

#converting/adding to list
number_list=[n1,n2,n3,n4,n5]

#converting to tuple
n_tuple = tuple(number_list)

#sorting
n_sort = sorted(number_list)

#displaying
print("This is your number list sorted : ", n_sort)

