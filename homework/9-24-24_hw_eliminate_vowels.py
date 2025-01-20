#vowels
string = "AEIOUaeiou"
#
vowel_count = 0
sentence_without_vowels = ""
sentence = input("Enter a sentence : ")

#main part
for char in sentence:
    if char in string:
        vowel_count += 1
    else:
        sentence_without_vowels += char

#printing:
print(f"\nOriginal sentence : {sentence}")
print(f"Number of vowels removed : {vowel_count}")
print(f"Sentence without vowels : {sentence_without_vowels}")