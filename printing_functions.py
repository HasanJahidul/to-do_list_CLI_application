import sys
# a menu for to-do list


def main_menu():
    print("""
    1. Add a new task
    2. Update an existing task
    3. Delete a task
    4. View all tasks
    5. Save tasks to file
    6. Search tasks
    7. Exit
    """)


def thanks():
    # A simple gesture of courtesy towards the user to enhance user experience
    print("********************************************************************")
    print("Thank you for using our Python To-Do List Application.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")
