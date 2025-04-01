# Inducil, Raphael Clouiee A.
# 4-01-25 
# batch 7, Prog08. count() returns how many times the function parameter 
# appears in the string. Create a program that does the same functionality 
# without using count() function.

# ask the user to enter a string

input_string = input("Enter a string: ")

# ask the user to enter the substring to count

substring = input("Enter the substring to count: ")

# initialize a counter variable to zero

count = 0

# get the length of the substring

substring_length = len(substring)

# loop through the string while checking each position for a match

for i in range(len(input_string) - substring_length + 1):
    
    # check if the substring matches the portion of the string
    
    if input_string[i:i + substring_length] == substring:
        
        # if a match is found, increment the counter
        
        count += 1

# print the total count of occurrences

print("The substring appears", count, "times in the string.")

# end