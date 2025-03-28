# Inducil, Raphael Clouiee A.
# 3-28-25
# batch 6, prog10: capitalize the first letter of each word in a string and convert all other letters to lowercase without using title()

# ask the user to enter a string

user_text = input("Enter a string: ")

# split the string into words
# capitalize the first letter of each word
# convert the rest of the letters in each word to lowercase

def title_case(text):
    """Manually capitalizes the first letter of each word and converts the rest to lowercase."""
    words = text.split()
    title_cased_words = []
    
    for word in words:
        if word:
            first_char = word[0]
            remaining_chars = word[1:]

            first_char = chr(ord(first_char) - 32) if 'a' <= first_char <= 'z' else first_char
            lowercase_text = "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in remaining_chars)
            title_cased_words.append(first_char + lowercase_text)

# join the modified words back into a single string

    return " ".join(title_cased_words)

# print the modified string

result = title_case(user_text)
print("Title-cased string:", result)

# end