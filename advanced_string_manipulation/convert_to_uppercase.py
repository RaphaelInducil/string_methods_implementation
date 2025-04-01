# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog03. upper() converts all characters of the string into upper case.
# Create a program that do the same functionality without using upper() function.

# ask the user to enter a string

input_string = input("Enter a string: ")

# initialize an empty string for the result

result = ""

# loop through each character of the string

for char in input_string:

    # convert each character to uppercase if it's a lowercase letter

    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)  # convert to uppercase by adjusting ASCII value
    else:
        result += char  # keep the character as is if it's not a lowercase letter

# print the modified string

print("Modified string:", result)

# end
