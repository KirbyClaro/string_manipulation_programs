#Prog02B6. removeprefix() remove the characters 
# at the beginning of the string that matches the 
# function parameter. Create a program that do 
# the same functionality without using 
# removeprefix() function.

user_input = input("Enter a string: ")
prefix = input("Enter a prefix: ")

def remove_prefix(user_input, prefix):
    if user_input.startswith(prefix):
        return user_input[len(prefix):]
    return user_input

result = remove_prefix(user_input, prefix)

print("The modified string is:", result)