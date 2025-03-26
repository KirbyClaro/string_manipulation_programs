#Prog02B6. removeprefix() remove the characters 
# at the beginning of the string that matches the 
# function parameter. Create a program that do 
# the same functionality without using 
# removeprefix() function.

# Get user input for the string and prefix
user_input = input("Enter a string: ")
prefix = input("Enter a prefix: ")

# Function to remove the prefix from the string
def remove_prefix(user_input, prefix):
    if user_input.startswith(prefix):
        return user_input[len(prefix):]
    return user_input

# Call the function and store the result in the variable "result"
result = remove_prefix(user_input, prefix)

# Print the modified string
print("The modified string is:", result)