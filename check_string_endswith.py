#Prog05B6. endswith() check if the string 
# end part matches the function parameter. 
# Create a program that do the same 
# functionality without using endswith() function.

# Prompt the user to enter a string and a suffix
user_input = input("Enter a string: ")
suffix = input("Enter a suffix: ")

# Function to check if the string ends with the given suffix
def check_endswith(user_input, suffix):
    return user_input[-len(suffix):] == suffix if len(suffix) <= len(user_input) else False

# Check if the string ends with the given suffix and display the result
if check_endswith(user_input, suffix):
    print("The string ends with the suffix.")
else:
    print("The string does not end with the suffix.")