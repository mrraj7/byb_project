# Practical task 4
#
# ========================================================= Pseudocode ==============================================================
# Below is the pseudocode to show the usage of casting functions in python
# Declare a variable num1 and assign the value 99.23
# Declare a variable num2 and assign the value 23
# Declare a variable num3 and assign the value 150
# Declare a variable string1 and assign the value "100"
# Convert num1 to integer using "int" casting function and store the value in a vairable called num1_integer
# Convert num2 to float using "float" casting function and store the value in a vairable called num2_float
# Convert num3 to string using "str" casting function and store the value in a vairable called num3_string
# Convert string1 to integer using "int" casting function and store the value in a vairable called string1_integer
# Store the input into a variable called "user_name"
# Finally output all the values stored in the variables using print statement with appropriate text
#
# ========================== Python code ==============================
# Declare variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"
# Convert float to integer
num1_integer = int(num1)
# Convert integer to float
num2_float = float(num2)
# Convert integer to string
num3_string = str(num3)
# Convert string to integer
string1_integer = int(string1)
# Print all the values stored in the variables
print("Float to integer conversion : ", num1, num1_integer)
print("Integer to Float conversion : ", num2, num2_float)
print("Integer to String coversion : ", num3, num3_string)
print("String to Integer conversion : ", string1, string1_integer)

