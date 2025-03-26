#Prog07B6. center() add space characters 
# at the beginning and at the end of the 
# string to print the string at the center. 
# Create a program that do the same functionality 
# without using center() function.

# Get user input
user_input = input("Enter a string: ")
width = int(input("Enter the total width: "))

# Add spaces to the left and right if the string length is less than the specified width
if len(user_input) < width:
    total_spaces = width - len(user_input)
    left_spaces = total_spaces //2
    right_spaces = total_spaces - left_spaces
    user_input = " " * left_spaces + user_input + " " * right_spaces\

# Display the modified string and added repr to show the added spaces
print("Result:", repr(user_input))