def square(size):
    if size < 2:
        print("size can't be less than 2")
        return
    for i in range(size):
        if i == 0 or i == size - 1:
            print("* " * size)
        else:
            print("* "+"  " * (size-2) + "*")


size = int(input("Enter the size of the square frame: "))
square(size)