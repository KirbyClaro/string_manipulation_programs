#Prog08. swapcase() reverse the casing of 
# each of the character of the string. 
# a program that do the same functionality 
# without using swapcase() function.

user_input = input("Enter a string: ")

result = ""
for char in user_input:
    if "a" <= char <= "z":
        result += chr(ord(char) - 32)  
    elif 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)  
    else:
        result += char

print("Reverse Casing:", result)