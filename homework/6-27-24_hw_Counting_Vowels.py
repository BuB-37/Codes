# Define the vowels
vowel = "aeiouAEIOU"

#Take inpout from the user
word = input("ENTER A WORD TO FIND OUT HOW MANY VOWELS IT HAS : ")
 
#Use a list comprehension to check each character in the word
# Sum up 1 for each vowel found in the word
num_vowels = sum(1 for char in word if char in vowel)

#Print the result
print(f"The number of vowels in '{word}' is {num_vowels}")