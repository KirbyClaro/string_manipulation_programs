#Prog09B6. capitalize() makes the first letter 
# of the string, capital letter. And all other 
# letter in small case. Create a program that 
# do the same functionality without using 
# capitalize() function.


# Function to capitalize the first letter of the string and convert the rest to lowercase
def capitalization(user_input):
    if len(user_input) == 0:
        return user_input
    return user_input[0].upper() + user_input[1:].lower()

# Get user input
user_input = input("Enter a string: ")

# Call the function and store the result in the variable "result"
result = capitalization(user_input)

# Print the capitalized string
print("Capitalized string: ", result)