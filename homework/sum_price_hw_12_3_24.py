total = []
for i in range(1,6):
    price = int(input("Enter price : "))
    total.append(price)

total_sum = sum(total)

print(f"Total Sum of the prices = {total_sum}")