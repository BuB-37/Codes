
def prime_number(start, end):
    prime = []
    for num in range(start, end + 1):
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            prime.append(num)
    return prime


start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Primes:", prime_number(start, end))