#Prog07. zfill() add zero characters at the 
#beginning of the string to complete the number 
#of characters specifies in function parameter. 
#Create a program that do the same functionality 
#without using zfill() function.

# Get user input for the string and total width
user_input = input("Enter a string: ")
total_width = int(input("Enter the total width: "))

# Add zero characters at the beginning if the string length is less than the specified width
while len(user_input) < total_width:
    user_input = "0" + user_input
    
# Display the modified string and added repr to show the added zeros
print("Result:", repr(user_input))