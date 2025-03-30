#Prog05B7. startswith() check if the string 
#beginning part matches the function parameter. 
#Create a program that do the same functionality 
#without using startswith() function.

#user input
user_input = input("Enter a string: ")
prefix = input("Enter a prefix: ")
matches = True

# Check if the string starts with the given prefix
if len(prefix) > len(user_input):
    matches = False
else:
    # compare characters one by one from both strings
    for i in range(len(prefix)):
        if user_input[i] != prefix[i]:
            matches = False
            break

# Display the result
print("Does the string match with the function parameter(prefix)?", matches)