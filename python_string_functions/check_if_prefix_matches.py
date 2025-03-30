#Prog05. startswith() check if the string 
#beginning part matches the function parameter. 
#Create a program that do the same functionality 
#without using startswith() function.

user_input = input("Enter a string: ")
prefix = input("Enter a prefix: ")
matches = True

if len(prefix) > len(user_input):
    matches = False
else:
    for i in range(len(prefix)):
        if user_input[i] != prefix[i]:
            matches = False
            break

print("Does the string match with the function parameter(prefix)?", matches)