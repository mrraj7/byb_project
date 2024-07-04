# ==================== Practical Task 1 ========================
# This program that reads the data from the text file provided (DOB.txt)
# and prints it out in two different sections ie, Name & Date of Birth

# Declare a list to store names and date of birth read from the given text file
names_list = []
dob_list = []

# Open and read the entire text file "DOB.txt" and store it in the list
with open('DOB.txt', 'r') as file:
    lines = file.read().splitlines()

# Using the for loop, for each element in the list determine the starting position 
# of date of birth and load and split the string and append name & date of birth list
for i in range(len(lines)):
    for j in lines[i]:
        if j.isnumeric():
            dob_position = lines[i].index(j)
            break
    names_list.append(lines[i][: dob_position - 1])
    dob_list.append(lines[i][dob_position: ])


# First print the names list extracted from the file#
print("Name")
print(*names_list, sep = "\n")

print("======================")

# Now, print the date of birth list extrated from the file
print("Birthdate")
print(*dob_list, sep = "\n")
