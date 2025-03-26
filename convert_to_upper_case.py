#Prog04. isupper() check if all characters of the string 
# is on upper case. Create a program that 
#do the same functionality without using isupper() function.

#user input
user_input = input("Enter a string: ")

# Function to convert uppercase to lowercase
def lower_user_input(user_input):
    result = "" 
    # Iterate over each character in the input string and convert uppercase letters to lowercase
    for char in user_input:
        # ord() function returns the Unicode code point of a character
        if 'A' <= char <= 'Z':  
            # Subtract 32 from the Unicode code point of the 
            # uppercase letter to get the lowercase letter's Unicode code point
            result += chr(ord(char) + 32)  
        else:
            result += char  
    return result

# Call the function and print the result
result = lower_user_input(user_input)
print("The lower case version of the string is:", result)