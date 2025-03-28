# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog03: convert all characters of the string into lowercase without using lower()

# ask the user to enter a string

user_text = input("Enter a string: ")

# initialize an empty string to store the lowercase result

def to_lowercase(text):
    """Manually converts all characters in a string to lowercase."""
    lowercase_text = ""

# iterate through each character in the string

    for char in text:
        if 'A' <= char <= 'Z':

# if the character is an uppercase letter, convert it to lowercase manually

            lowercase_text += chr(ord(char) + 32)
        else:
            lowercase_text += char
    return lowercase_text

# append the character to the new string
# print the modified string

result = to_lowercase(user_text)
print("String in lowercase:", result)

# end