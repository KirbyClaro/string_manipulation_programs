#Prog06B6. ljust() add space characters at the 
# end of the string to complete the number 
# of characters specifies in function parameter. 
# Create a program that do the same functionality 
# without using ljust() function.

# Get user input
user_input = input("Enter a string: ")
width = int(input("Enter the total width: "))

# Add spaces to the right if the string length is less than the specified width
if len(user_input) < width:
    user_input += " " * (width - len(user_input))  # Add spaces to the right

# Display the modified string and added repr to show the added spaces
print("Result:", repr(user_input))
