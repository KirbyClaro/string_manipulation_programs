#Prog09B6. capitalize() makes the first letter 
# of the string, capital letter. And all other 
# letter in small case. Create a program that 
# do the same functionality without using 
# capitalize() function.

user_input = input("Enter a string: ")
result = capitalization(user_input)

def capitalization(user_input):
    if len(user_input) == 0:
        return user_input
    return user_input[0].upper + user_input[1:].lower

print("Capitalized string: ", result)