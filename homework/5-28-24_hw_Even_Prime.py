prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
print("prime numbers")
print("")
print("even numbers")
print("")
# Create sets from the lists
prime_set = set(prime_numbers)
even_set = set(even_numbers)

# Perform set operations
union_set = prime_set.union(even_set)
intersection_set = prime_set.intersection(even_set)
difference_set = prime_set.difference(even_set)
symmetric_difference_set = prime_set.symmetric_difference(even_set)

# Print the results
print("Prime numbers:", prime_numbers)
print("")
print("Even numbers:", even_numbers)
print("")
print("Union:", union_set)
print("")
print("Intersection:", intersection_set)
print("")
print("Difference (primes - evens):", difference_set)
print("")
print("Symmetric difference:", symmetric_difference_set)