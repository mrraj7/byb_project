# ====================== Auto graded Task 1 ===================
# This program ask the user to enter a string and manipulate the string using string functions
str_manip = str(input("Enter a string : "))
#
# Determine the length of the string and print the output
# string_length = len(str_manip)
# print("The length of the string is :", string_length)
# #
# # Find the last character of the string and replace that character with "@"
# string_last_chr = str_manip[-1:]
# replaced_string = str_manip.replace(string_last_chr,"@")
# print("This is the modified string :", replaced_string)
# #
# # Print last three characters from the input string
# print("Last three charaters in the input string : ",str_manip[:-4:-1])
# #
# # Create a new word from first three characters and last 2 characters
# new_word = str_manip[:3] + str_manip[string_length - 2:]
# print("Word from first three characters and last 2 characters :", new_word)
# Get sentence to manipulate
str_manip = input("Enter a sentence:\n")

# Display the length of the sentence and print it
print(len(str_manip))

# Find the last character in the sentence
last_letter = str_manip[-1]

# Replace every occurrence of the last letter in str_manip with "@"
print(str_manip.replace(last_letter, "@"))

# Print the last 3 characters backwards
print(str_manip[-1:-4:-1])

# A 5-letter word made up of the first 3 letters and the last 2 letters
print(str_manip[:3] + str_manip[-2:])