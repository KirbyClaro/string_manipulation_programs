#Prog07. zfill() add zero characters at the 
#beginning of the string to complete the number 
#of characters specifies in function parameter. 
#Create a program that do the same functionality 
#without using zfill() function.

user_input = input("Enter a string: ")
total_width = int(input("Enter the total width: "))

while len(user_input) < total_width:
    user_input = "0" + user_input

print("Result:", repr(user_input))