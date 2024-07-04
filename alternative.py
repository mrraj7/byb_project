# =================================== Practical Task 1 ==================================
# This program that reads in a string and makes each alternate character into an 
# upper case character and each other alternate character a lower case character.
# Also,convert each alternative word in the given string to lower case and upper case

# Get the string as an input from the user
str1 = input("Enter a string : ")

# Conver the string to list
str1_list = list(str1)

# Using for loop convert the each alternate character in the list to uppercase and lowercase
for i in range(0,len(str1)):
    if i % 2 == 0:
        str1_list[i] = str1_list[i].upper()
    else:
        str1_list[i] = str1_list[i].lower()

# Print the output as string using join method
print("".join(str1_list))

# Now use the same input string and convert each alternative word to lower and upper case

# Using split method split the words in the string and create as a list
list_of_words = str1.split()

# Using for loop convert the each word in the list to lowercase and uppercase
for i in range(0,len(list_of_words)):
    if i % 2 == 0:
        list_of_words[i] = list_of_words[i].lower()
    else:
        list_of_words[i] = list_of_words[i].upper()

# Print the output as string using join method with a blank character in between words
print(" ".join(list_of_words))
