# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog07: add space characters at the beginning and at the end of the string to print it at the center without using center()

# ask the user to enter a string
# ask the user to enter the total width of the final string

user_text = input("Enter a string: ")
width = int(input("Enter the total width: "))

# get the length of the original string

def center_align(text, width):
    """Manually centers a string by adding spaces on both sides to match the specified width."""
    text_length = len(text)
    if text_length >= width:
        return text
    
# calculate the number of spaces needed on each side to center the string

    total_spaces = width - text_length
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

# append spaces to both sides of the string

    return " " * left_spaces + text + " " * right_spaces  # Append spaces on both sides

# print the modified string

result = center_align(user_text, width)
print("Centered string:", repr(result))

# end