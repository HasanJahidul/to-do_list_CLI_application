from printing_functions import thanks,main_menu
todo_list = []

# handle the operation of the program
def add_task():
    task = input("Enter a new task: ")
    todo_list.append(["", "", "", "",""])
    todo_list[-1][0] = task
    todo_list[-1][1] = input("Enter a date in YYYY-MM-DD format: ")
    todo_list[-1][2] = input("Enter a Start time in HH:MM format: ")
    todo_list[-1][3] = input("Enter the End time in HH:MM format: ")
    todo_list[-1][4] = input("Enter the description: ")
    print("\nTask added successfully!")
    main_menu()
    user_input()

def update_task():
    task_or_date = input("Enter a task or date: ")
    # search in list and print index
    for index, task in enumerate(todo_list):
        if task[0] == task_or_date or task[1] == task_or_date:
            #update the task
            todo_list[index][0] = input("Enter the Updated task: ")
            todo_list[index][1] = input("Enter the Updated in YYYY-MM-DD format: ")
            todo_list[index][2] = input("Enter the Updated Start time in HH:MM format: ")
            todo_list[index][3] = input("Enter the Updated End time in HH:MM format: ")
            todo_list[-1][4] = input("Enter the description: ")
            print("\nTask Updated successfully!")
    main_menu()
    user_input()

def delete_task():
    task_or_date = input("Enter a task or date: ")
    for index, task in enumerate(todo_list):
        if task[0] == task_or_date or task[1] == task_or_date:
            todo_list.pop(index)
            print("Task deleted successfully!")
    main_menu()
    user_input()
    

def view_all():
    print ("{:<10} {:<20} {:<20} {:<20} {:<20}".format('Task','Date','Start Time','End Time','Description'))
    for item in todo_list:
        task, date, start_time,end_time,des = item
        print ("{:<10} {:<20} {:<20} {:<20} {:<20}".format(task, ''.join(map(str, date)), ''.join(map(str, start_time)), ''.join(map(str, end_time)),''.join(map(str, des))))  
    main_menu()
    user_input()

def operation(operation_type, operation_value, operation_list):
    if operation_type == "delete":
        # delete task
        operation_list.pop(operation_value)
    elif operation_type == "view":
        print(operation_list)
    elif operation_type == "save":
        with open("todo.txt", "w") as file:
            for item in operation_list:
                file.write(item + "\n")
    elif operation_type == "search":
        for item in operation_list:
            if operation_value in item:
                print(item)
    elif operation_type == "exit":
        print("Goodbye!")
    else:
        print("Invalid operation")


def user_input():
    menu = input("Enter your choice: ")
    while menu != "7":
        if menu == "1":
            add_task()
        elif menu == "2":
           update_task()
        elif menu == "3":
            delete_task()
        elif menu == "4":
           view_all()
        elif menu == "5":
            operation("save", None, todo_list)
        elif menu == "6":
            task = input("Enter the task you want to search: ")
            operation("search", task, todo_list)
        else:
            print("Invalid choice")
        menu = input("Enter your choice: ")
    thanks()
