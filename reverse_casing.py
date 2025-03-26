#Prog08B6. swapcase() reverse the casing of 
# each of the character of the string. 
# a program that do the same functionality 
# without using swapcase() function.

# Get user input for the string
user_input = input("Enter a string: ")

# Reverse the casing of each character in the string
result = ""
for char in user_input:
    if "a" <= char <= "z":
        #Turn Lowercase to  Uppercase
        result += chr(ord(char) - 32)  
    elif 'A' <= char <= 'Z':
        # Turn Uppercase to Lowercase
        result += chr(ord(char) + 32)  
    else:
        result += char

# Display the modified string
print("Reverse Casing:", result)