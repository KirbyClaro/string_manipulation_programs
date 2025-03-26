#Prog01B6. lstrip() remove the space characters at the beginning 
#of the string. Create a program that do the same 
#functionality without using lstrip() function.

# Function to remove leading spaces 
def remove_leading_spaces(text):
    # Start from the beginning of the string and remove spaces
    position = 0
    # Continue until a non-space character is found or the end of the string is reached
    while position < len(text):
        if text[position] != ' ':  # Found a non-space character
            break
        position += 1
    # Return the remaining characters after removing the leading spaces
    return text[position:]

# Take user input for the text string
text = input("Enter a text: ")

# Display the original and modified strings 
print ("\n This is the original text:",repr(text))
print ("\n This is the new text:",repr(remove_leading_spaces(text)))