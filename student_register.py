# This program allows a user to register student id details for an exam venue

# First ask the user to enter how many students are registering
number_of_students = int(input("How many students are registering? : "))

# Now for the total number of students ask the user to input 
# each student id and write into a text file called 'reg_form.txt'
# Also add a dotted line after each student id in the text file for signature 
with open('reg_form.txt', 'w') as file:
    for i in range (0,number_of_students):
        student_id = str(input("Enter the student id : "))
        file.write(student_id + " ......................" + "\n")
