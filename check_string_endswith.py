#Prog05B6. endswith() check if the string 
# end part matches the function parameter. 
# Create a program that do the same 
# functionality without using endswith() function.

user_input = input("Enter a string: ")
suffix = input("Enter a suffix: ")

def check_endswith(user_input, string):
    return user_input[-len(suffix)] == suffix if len(suffix) <= len(user_input) else False

if check_endswith(user_input, suffix):
    print("The string ends with the suffix.")
else:
    print("The string does not end with the suffix.")