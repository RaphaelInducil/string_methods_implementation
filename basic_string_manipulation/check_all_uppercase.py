# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog04: check if all characters of the string are uppercase without using isupper()

# ask the user to enter a string

user_text = input("Enter a string: ")

# iterate through each character in the string
# check if each character is an uppercase letter

def is_all_uppercase(text):
    """Manually checks if all characters in a string are uppercase."""
    for char in text:
        if 'a' <= char <= 'z':

# if any character is not uppercase, return false
# if all characters are uppercase, return true

            return False
    return True

# print the result

result = is_all_uppercase(user_text)
print("Is the string all uppercase?:", result)

# end