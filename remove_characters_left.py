#Prog01. lstrip() remove the space characters at the beginning 
#of the string. Create a program that do the same 
#functionality without using lstrip() function.

def remove_leading_spaces(text):
    position = 0
    while position < len(text):
        if text[position] != ' ':  # Found a non-space character
            break
        position += 1
    return text[position:]

text = input("Enter a text: ")

print ("\n This is the original text:",repr(text))
print ("\n This is the new text:",repr(remove_leading_spaces(text)))