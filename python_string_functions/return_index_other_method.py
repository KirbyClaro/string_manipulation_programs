#Prog10B7. rindex() return the first location of 
#the function parameter in the string starting 
#from the last character. Create a program that 
#do the same functionality without using rindex() function.

#user input
user_input = input("Enter a string: ")
character_finder = input("Enter a character to find: ")

# find the first occurrence of the character in the string and store its index
index = -1 

for i in range(len(user_input)-1, -1, -1):
    if user_input[i] == character_finder:
        index = i
        break
    
print("Last occurrence index:", index)