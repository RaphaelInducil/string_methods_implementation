# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog02. removesuffix() remove the characters at the end of the string 
# that matches the function parameter. Create a program that do the same functionality 
# without using removesuffix() function.

# ask the user to enter a string

input_string = input("Enter a string: ")

# ask the user to enter a suffix to remove

suffix = input("Enter the suffix to remove: ")

# check if the string ends with the given suffix

if input_string.endswith(suffix):

    # if the string ends with the suffix, slice the string to remove the suffix

    modified_string = input_string[:-len(suffix)]
else:
    modified_string = input_string

# print the modified string

print("Modified string:", modified_string)

# end