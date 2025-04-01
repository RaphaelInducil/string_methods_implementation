# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog07. zfill() adds zero characters at the beginning of the string 
# to complete the number of characters specified in the function parameter.
# Create a program that does the same functionality without using zfill() function.

# ask the user to enter a string

input_string = input("Enter a string: ")

# ask the user to enter the total width of the output string

total_width = int(input("Enter the total width: "))

# calculate the number of zeros needed at the beginning

num_zeros = total_width - len(input_string)

# ensure the number of zeros is not negative

if num_zeros < 0:
    num_zeros = 0

# create a new string with the required zeros followed by the original string

zero_filled_string = "0" * num_zeros + input_string

# print the zero-filled string

print("Zero-filled string:", zero_filled_string)

# end