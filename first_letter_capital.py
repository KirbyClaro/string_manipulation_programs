#Prog10. title() makes all first letter of 
# each word in the string, capital letter. 
# And all other letter in small case. Create a 
# program that do the same functionality without 
# using title() function.

user_input = input("Enter a string: ")

split_input = user_input.split()
new_words = []

for word in split_input:
    new_word = word[0].upper() + word[1:].lower() if word else "" 
    new_words.append(new_word)\

result = " ".join(new_words)
print("Result: " + result)