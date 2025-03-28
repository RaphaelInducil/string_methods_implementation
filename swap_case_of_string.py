# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog08: reverse the casing of each character in the string without using swapcase()

# ask the user to enter a string

user_text = input("Enter a string: ")

# initialize an empty string to store the swapped case result

def swap_case(text):
    """Manually swaps the case of each character in the string."""
    swapped_text = ""

# iterate through each character in the input string
# if the character is uppercase, convert it to lowercase

    for char in text:
        if 'A' <= char <= 'Z':
            swapped_text += chr(ord(char) + 32)

# if the character is lowercase, convert it to uppercase

        elif 'a' <= char <= 'z':
                swapped_text += chr(ord(char) - 32)

# concatenate the modified characters to form the final string

        else:
            swapped_text += char
    return swapped_text

# print the modified string

result = swap_case(user_text)
print("Swapped case string:", result)

# end