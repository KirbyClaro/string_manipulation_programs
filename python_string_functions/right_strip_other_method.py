#Prog01. rstrip() remove the space characters 
# at the end of the string. Create a 
# program that do the same functionality 
# without using rstrip() function.

user_input = input("Enter a string: ")
while len(user_input) > 0 and user_input[-1] == " ":
    user_input = user_input[:-1]
    
print("String after removing trailing spaces:", user_input)