# =========================================  Auto-graded Task =================================================
# This program creates an email simulator using OOP. It has a class Email with constructor method to initialize
# instance variables and a method to mark the email that it has been read.
#
# The program asks the user to input an option from the below menu:
#    1. Read an email
#    2. View unread emails
#    3. Quit application
# and then calls appropriate function to perform an action based on the user input.
# =========================================  Auto-graded Task =================================================

# Define a Email class with three attributes ie., email_address, subject_line and email_content
class Email:

    # Class variables
    has_been_read = False

    # Constructor method with instance variables email_address, subject_line and email_content
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Method to edit the values of the email objects
    def mark_as_read(self):
        return True

def populate_inbox(email, subject, content):
    inbox.append(Email(email, subject, content))

# This function list the unread email index and subject line
def list_emails():
    print("These are the subject line(s) of the unread emails :")
    print("----------------------------------------------------")
    for count, element in enumerate(inbox):
        if not element.has_been_read:
            print(count, element.subject_line)
    print("----------------------------------------------------")

# This function list the email details such as email address, email subject line and email content
def read_email(email_index):
    print(f"Email address : {inbox[email_index].email_address}")
    print(f"Subject line : {inbox[email_index].subject_line}")
    print(f"Email content : {inbox[email_index].email_content}")
    inbox[email_index].has_been_read = inbox[email_index].mark_as_read()

# This function performs an action based on the chosen option from the menu
# If option is 1, then call a function to list all unread emails and ask the user to enter the index of the email to be read
# If option is 2, call the function to list all the unread email in inbox
def action(chosen_option):
    if chosen_option == 1:
        list_emails()
        index = int(input("Enter the index of the email to be read : "))
        read_email(index)
    elif chosen_option == 2:
        list_emails()

# Create an list in a called inbox
inbox = []

# Call populate_inbox function to build a list of 3 objects
populate_inbox("raj1@gmail.com", "Welcome to HyperionDev!", "Greetings! Congratulations on taking Bootcamp")
populate_inbox("raj2@gmail.com", "Great work on the bootcamp!", "Greetings! Well done. Keep it up") 
populate_inbox("raj3@gmail.com", "Your excellent marks!", "Greetings! Congratulation on completing tasks")

# Display the menu option and get the user input
while True:
    print("======================================")
    print("Choose one of the following options : ")
    print("======================================")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    print("======================================")
    option = int(input())

    # Check the option and take action accordingly
    if option < 1 or option > 3:
        print("Option not valid. Enter a valid option number ")
    elif option == 1 or option == 2:
        action(option)
    else:
        print("Quiting application ...")
        break
