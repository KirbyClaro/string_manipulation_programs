#Prog06. rjust() add space characters 
# at the beginning of the string to 
# complete the number of characters 
# specifies in function parameter. 
# Create a program that do the same 
# functionality without using rjust() function.

user_input = input("Enter a string: ")
total_width = input("Enter total width: ")

while len(user_input) < total_width:
    user_input = ' ' + user_input

print("This is the right justified string: ", repr(user_input))