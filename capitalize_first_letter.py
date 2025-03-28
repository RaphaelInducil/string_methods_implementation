# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog09: capitalize the first letter of the string and convert all other letters to lowercase without using capitalize()

# ask the user to enter a string

user_text = input("Enter a string: ")

# check if the string is not empty
# convert the first character to uppercase

def capitalize_text(text):
    """Manually capitalizes the first letter of the string and converts the rest to lowercase."""
    if not text:
        return text
    
    first_char = text[0] 
    remaining_chars = text[1:]

# convert the rest of the characters to lowercase

    capitalized_text = chr(ord(first_char) - 32) if 'a' <= first_char <= 'z' else first_char
    lowercase_text = "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in remaining_chars)
    
# concatenate the modified characters to form the final string

    return capitalized_text + lowercase_text

# print the modified string

result = capitalize_text(user_text)
print("Capitalized string:", result)

# end
