# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# ask the user to enter a string
input_string = input("Enter a string: ")

# initialize an empty string for the result
result = ""

# loop through the string from the end

for char in reversed(input_string):

# remove space characters from the end until a non-space character is found
  
    if char != " ":
        result = char + result
    else:
        if result != "":  # stop when a non-space character is found
            result = char + result

# return the modified string
# print the modified string

print("Modified string:", result)

# end