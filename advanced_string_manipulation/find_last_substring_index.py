# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog10. rindex() returns the first location of the function parameter 
# in the string starting from the last character. Create a program that does 
# the same functionality without using rindex() function.

# ask the user to enter a string

input_string = input("Enter a string: ")

# ask the user to enter the substring to find

substring = input("Enter the substring to find: ")

# get the length of the substring

substring_length = len(substring)

# initialize a variable to store the index, set to -1 (not found)

last_index = -1

# loop through the string in reverse order while checking each position for a match

for i in range(len(input_string) - substring_length, -1, -1):
    
    # check if the substring matches the portion of the string
    
    if input_string[i:i + substring_length] == substring:
        
        # store the index and break the loop
        
        last_index = i
        break

# check if the substring was found and print the result

if last_index != -1:
    print("The substring last appears at index:", last_index)
else:
    print("Substring not found in the string.")

# end