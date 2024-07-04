# Practical task 3
#
# ========================================================= Pseudocode ==============================================================
# Below is the pseudocode to get the user name, age, House number & Street name as input and to print that as output
# First, request the user name as input
# Store the input into a variable called "user_name"
#
# Next, request the user age as input
# Store the age into a variable called "user_age"
#
# Next, request the House number as input
# Store the house number into a variable called "house_number"
#
# Next, request the street name as input
# Store the age into a variable called "street_name"
#
# Output the values stored in the above variables in a single sentence as given in the below example 
# Example "This is John Smith. He is 28 years old and lives at house number 42 on Hamilton Street."
#
# ========================== Python code ==============================
# ========= Getting user name as input and print the user name =========
user_name = input("Enter the user name : ")
# ========= Getting age as input from the user and print the age =========
user_age = input("Enter the age : ")
# ========= Getting House number as input from the user =========
house_number = input("Enter the House number : ")
# ========= Getting street name as input from the user  =========
street_name = input("Enter the Street name : ")
# ========= Print the user details stored in the variables in a single sentence =========
print("This is " + user_name + ". He/She is " + str(user_age) + " years old and lives at house number " + str(house_number) + " on " + street_name + ".")
