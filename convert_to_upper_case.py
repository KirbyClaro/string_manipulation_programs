#Prog04B6. isupper() check if all characters of the string 
# is on upper case. Create a program that 
#do the same functionality without using isupper() function.

#user input
user_input = input("Enter a string: ")

# Function to convert uppercase to lowercase
def upper_user_input(user_input):
    result = "" 
    # Iterate over each character in the input string and convert lower letters to uppercase
    for char in user_input:
        # Convert lowercase letters to uppercase using ASCII values
        if 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)  
        else:
            result += char  
    return result

# Call the function and print the result
result = upper_user_input(user_input)
print("The uppercase version of the string is:", result)