#Prog01B7. rstrip() remove the space characters 
# at the end of the string. Create a 
# program that do the same functionality 
# without using rstrip() function.

#user input
user_input = input("Enter a string: ")

# remove the trailing spaces using a loop
while len(user_input) > 0 and user_input[-1] == " ":
    user_input = user_input[:-1]
    
# print the resulting string
print("String after removing trailing spaces:", repr(user_input))