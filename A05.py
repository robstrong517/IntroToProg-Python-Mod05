# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #
# Define the Data Constants
import json

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file: None    # Holds a reference to an opened file.
menu_choice: str = '' # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print("Creating new file...")
    file = open(FILE_NAME, "w")
    print(e, e.__doc__, type(e), sep='\n')

except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print("Resetting session data...")
    students = []
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain letters.")
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain letters.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"first_name": student_first_name, "last_name": student_last_name, "course_name": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)

        continue

    # Present the current data
    elif menu_choice == "2":
        for student in students:
        # Process the data to create and display a custom message
            print("-"*50)

            print(f'Student {student["first_name"]} {student["last_name"]} is enrolled in {student["course_name"]}')

            print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")
            ##ENSURE THAT THE ENTIRE STUDENTS LIST IS ADDED TO THE JSON FILE
            ##.dump() WRITES ONLY DICTIONARIES OR LISTS OF DICTIONARIES, NOT STRINGS. data IS A STRING RIGHT NOW

            json.dump(students, file)
            for student in students:
                    ##item IS THE VARIABLE YOU CHOSE FOR EACH INDIVIDUAL DICTIONARY, NOT student
                    print(f"Student {student["first_name"]} {student["last_name"]} is enrolled in {student["course_name"]}!")
            file.close()
        except Exception as e:
            print("Error saving data to file.")
            print(e)
        finally:
            if file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
