# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog06: add space characters at the end of the string to complete the specified length without using ljust()

# ask the user to enter a string
# ask the user to enter the total width of the final string

user_text = input("Enter a string: ")
width = int(input("Enter the total width: "))

# get the length of the original string

def left_justify(text, width):
    """Manually adds spaces to the end of a string to match the specified width."""
    text_length = len(text)

# calculate the number of spaces needed to reach the specified width

    if  text_length >= width:
        return text

# append the required number of spaces to the string

    spaces_needed = width - text_length
    return text + " " * spaces_needed

# print the modified string

result = left_justify(user_text, width)
print("Left-justified string:", repr(result))

# end
