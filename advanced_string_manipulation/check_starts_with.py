# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog05. startswith() checks if the beginning part of the string matches 
# the function parameter. Create a program that does the same functionality 
# without using startswith() function.

# ask the user to enter a string

input_string = input("Enter a string: ")

# ask the user to enter a prefix to check

prefix = input("Enter the prefix to check: ")

# get the length of the prefix

prefix_length = len(prefix)

# extract the beginning part of the string with the same length as the prefix

start_part = input_string[:prefix_length]

# compare the extracted part with the prefix

is_starting_with_prefix = start_part == prefix

# print whether the string starts with the given prefix

print("Does the string start with the given prefix?", is_starting_with_prefix)

# end