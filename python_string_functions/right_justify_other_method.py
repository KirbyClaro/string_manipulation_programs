#Prog06. rjust() add space characters 
# at the beginning of the string to 
# complete the number of characters 
# specifies in function parameter. 
# Create a program that do the same 
# functionality without using rjust() function.

# Get user input for the string and total width
user_input = input("Enter a string: ")
total_width = int(input("Enter total width: "))

# Add space characters at the beginning to make the string length equal to total width
while len(user_input) < total_width:
    user_input = " " + user_input

# Display the modified string and added repr to show the added spaces
print("This is the right justified string: ", repr(user_input))