# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog04. islower() checks if all characters of the string are in lowercase.
# Create a program that does the same functionality without using islower() function.

# ask the user to enter a string

input_string = input("Enter a string: ")

# initialize a variable to track if all characters are lowercase

is_lower = True

# loop through each character in the string

for char in input_string:
    
    # check if the character is an uppercase letter
    
    if 'A' <= char <= 'Z':
        
        # if an uppercase letter is found, set the variable to False and break the loop
        
        is_lower = False
        break

# print whether the string is entirely in lowercase

print("Is the string in lowercase?", is_lower)

# end