# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog02: remove the characters at the beginning of the string that match the given prefix without using removeprefix()

# Ask the user to enter a string
# Ask the user to enter a prefix to remove

user_text = input("Enter a string: ")
prefix_to_remove = input("Enter the prefix to remove: ")

# Check if the string starts with the given prefix
# If it does, remove the prefix by slicing the string

def remove_prefix(text, prefix):
    """Manually removes the given prefix from a string."""
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

# Print the modified string

result = remove_prefix(user_text, prefix_to_remove)
print("String after removing prefix:", result)


# End