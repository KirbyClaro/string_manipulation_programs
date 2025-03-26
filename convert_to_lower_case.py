#Prog03B6. lower() converts all characters 
# of the string into lower case. 
# Create a program that do the same 
# functionality without using lower() function.

user_input = input("Enter a string: ")

def lower_user_input(user_input):
    result = ""
    for char in user_input:
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
        return result

result = lower_user_input(user_input)
print("The lower case version of the string is:", lower_user_input(user_input))