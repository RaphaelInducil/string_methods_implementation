# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog06. rjust() adds space characters at the beginning of the string 
# to complete the number of characters specified in the function parameter.
# Create a program that does the same functionality without using rjust() function.

# ask the user to enter a string

input_string = input("Enter a string: ")

# ask the user to enter the total width of the output string

total_width = int(input("Enter the total width: "))

# calculate the number of spaces needed at the beginning

num_spaces = total_width - len(input_string)

# ensure the number of spaces is not negative

if num_spaces < 0:
    num_spaces = 0

# create a new string with the required spaces followed by the original string

right_justified_string = " " * num_spaces + input_string

# print the right-justified string

print("Right-justified string:", right_justified_string)
