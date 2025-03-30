#Prog08B7. count() return how many time 
#the function parameter appear in the string. 
#Create a program that do the same functionality 
#without using count() function.

user_input = input("Enter a string: ")
character_count = input("Enter a character to count: ")
count = 0

for c in user_input:
    if c == character_count:
        count += 1

print("The character", character_count, "appears", count, "times in the string.")