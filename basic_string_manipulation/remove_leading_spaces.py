# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog01: remove the space characters at the beginning of the string without using lstrip()

# ask user to input a string with leading spaces

user_input = input("Enter a string with leading spaces: ")

# iterate through the string to find the first non-space character

def remove_leading_spaces(text):
    """Manually removes leading spaces from a string."""
    for i, char in enumerate(text):
        if char != " ":
            return text[i:]
    return ""  

# create a new string starting from the first non-space character
# print the new string without leading spaces

cleaned_text = remove_leading_spaces(user_input)
print("String without leading spaces:", cleaned_text)

# end