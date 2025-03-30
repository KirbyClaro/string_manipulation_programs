#Prog02B7. removesuffix() remove the 
#characters at the end of the string 
#that matches the function parameter. 
#Create a program that do the same 
#functionality without using removesuffix() function.

# Get user input for the string and suffix
user_input = input("Enter a string: ")
suffix = input("Enter a suffix to remove")

# Check if the suffix exists in the string
if user_input.endswith(suffix):
    user_input = user_input[:len(user_input)-len(suffix)]
    
#print user_input
print("String after removing suffix:", user_input)