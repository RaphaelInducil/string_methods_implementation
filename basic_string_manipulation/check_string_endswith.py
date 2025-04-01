# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog05: check if the string end part matches the function parameter without using endswith()

# ask the user to enter a string
# ask the user to enter the ending substring to check 

user_text = input("Enter a string: ")
ending_substring = input("Enter the ending substring to check: ")

# get the length of the ending substring

def ends_with(text, ending):
    """Manually checks if a string ends with a given substring."""
    text_length = len(text)
    ending_length = len(ending)

# compare the last characters of the string with the ending substring

    if text_length < ending_length:
        return False

# if they match, return true

    return text[-ending_length:] == ending

# otherwise, return false
# print the result

result = ends_with(user_text, ending_substring)
print("Does the string end with the given substring?:", result)

# end