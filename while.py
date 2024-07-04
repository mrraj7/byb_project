# ===================== Practical Task 1 =====================
# Declare variables count, total and num
count = 0
total = 0

# Use while loop to get input from the user and total the numbers and increase the counter
while True:
    num = int(input("Enter a number : "))
    if num == -1:
        break
    count = count + 1
    total = total + num

# Print the average
print(f"Average of the numbers : {total / count}")
