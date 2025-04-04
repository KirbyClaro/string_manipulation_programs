#Prog09B7. index() return the first 
#location of the function parameter in the string. 
#Create a program that do the same functionality 
#without using index() function.

#user input
user_input = input("Enter a string: ")
character_finder = input("Enter a character to find: ")

# find the first occurrence of the character in the string and store its index
index = -1 

# iterate over each character in the string and check if it matches the character_finder
for i in range(len(user_input)):
    # if found, set the index and break the loop
    if user_input[i] == character_finder:
        index = i
        break

# print the result
print("Index of the first occurrence of", character_finder, "is:", index)