#Prog04B7. islower() check if all 
# characters of the string is on lower case. 
# Create a program that do the same functionality 
# without using islower() function.

user_input = input("Enter a string: ")
is_lower = True

# iterate over each character in the input string and check if any character is uppercase
for char in user_input:
    if 'A' <= char <= 'Z':
        is_lower = False
        break

#print is_lower
print("Is the string all lowercase?", is_lower)