# Function to generate the pattern
def print_pattern(rows):
    # First Quadrant (Upper Left Triangle)
    for i in range(1, rows + 1):
        print("*" * i, end=" " * (rows + 2 - i))
        print(" " * (rows + 2 - i), end="")
        print("*" * i)
         
    # Second Quadrant (Lower Left Triangle)
    for i in range(rows, 0, -1):
        print("*" * i, end=" " * (rows + 2 - i))
        print(" " * (rows + 2 - i), end="")
        print("*" * i)

# Input for number of rows
rows = int(input("Enter number of rows in 1st Quadrant: "))
print_pattern(rows)