def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

user_string = input("Enter a word : ")
reversed_string = reverse(user_string)

print("User string : ",user_string," Revered string : ",reversed_string)