#Prog09B7. index() return the first 
#location of the function parameter in the string. 
#Create a program that do the same functionality 
#without using index() function.

user_input = input("Enter a string: ")
character_finder = input("Enter a character to find: ")
index = -1 

for i in range(len(user_input)):
    if user_input[i] == character_finder:
        index = i
        break

print("Index of the first occurrence of", character_finder, "is:", index)