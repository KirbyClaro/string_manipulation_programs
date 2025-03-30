#Prog03B7. upper() converts all characters 
#of the string into upper case. 
#Create a program that do the same 
#functionality without using upper() function.

# Get user input for the string
user_input = input("Enter a string: ")
uppercase_user_input = ""

# Convert lowercase letters to uppercase by subtracting 32 from their ASCII values
for char in user_input:
    if 'a' <= char <= 'z':  
        uppercase_user_input += chr(ord(char) - 32)
    else:
        uppercase_user_input += char
        
# Display the modified string
print("Uppercase string:", uppercase_user_input)