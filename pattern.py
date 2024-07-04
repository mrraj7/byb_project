# ============================ Practical Task 2 =============================
# This program creates the below pattern using For loop and If-Else statement
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
#
# Assign the string "*****" to a variable
pattern = "*****"
# Use For loop and If-Else statement to slice the string stored in variable pattern and print the output
for x in range(0,10):
    if x <= 5:
        print(pattern[:x])
    else:
        print(pattern[:5-x])
