#Prog02B7. removesuffix() remove the 
#characters at the end of the string 
#that matches the function parameter. 
#Create a program that do the same 
#functionality without using removesuffix() function.

user_input = input("Enter a string: ")
suffix = input("Enter a suffix to remove")

if user_input.endswith(suffix):
    user_input = user_input[:len(user_input)-len(suffix)]