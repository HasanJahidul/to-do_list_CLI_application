from printing_functions import thanks, main_menu
import datetime
import time
todo_list = []

# handle the operation of the program

def add_to_list(description,start_epoch_time, end_epoch_time, address):
    todo_list.append(["","","",""])
    todo_list[-1][0] = description
    todo_list[-1][1] = start_epoch_time
    todo_list[-1][2] = end_epoch_time
    todo_list[-1][3] = address

def add_task():
    description = input("Enter a new task: ")
    
    date= input("Enter a date in YYYY-MM-DD format: ")
    s_time= input("Enter a Start time in HH:MM format: ")
    e_time= input("Enter the End time in HH:MM format: ")
    address= input("Enter the address: ")
    start_epoch_time, end_epoch_time = epoch_time(date, s_time, e_time)
    print(start_epoch_time, end_epoch_time)
    if (start_epoch_time > end_epoch_time):
        print("Start time should be less than end time")
        # todo_list.pop(-1)
    else:
        if todo_list:
            for index, task in enumerate(todo_list):
                if task[1]<=start_epoch_time and task[2]>=start_epoch_time:
                    print(task)
                    print("Start time should be greater than previous task end time")
                    # todo_list.pop(-1)
                    # print("list is not empty")
                    break
        else:
            print("list is empty")
            add_to_list(description, start_epoch_time, end_epoch_time, address)
            
            print("\nTask added successfully!")
    main_menu()
    user_input()


def update_task():
    task_or_date = input("Enter a task or date: ")
    # search in list and print index
    for index, task in enumerate(todo_list):
        if task[0] == task_or_date or task[1] == task_or_date:
            # update the task
            todo_list[index][0] = input("Enter the Updated task: ")
            todo_list[index][1] = input(
                "Enter the Updated in YYYY-MM-DD format: ")
            todo_list[index][2] = input(
                "Enter the Updated Start time in HH:MM format: ")
            todo_list[index][3] = input(
                "Enter the Updated End time in HH:MM format: ")
            todo_list[index][4] = input("Enter the address: ")
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
    print("{:<10} {:<20} {:<20} {:<20} {:<20}".format(
        'Description', 'Date', 'Start Time', 'End Time', 'Place'))
    for item in todo_list:
        task, date, start_time, end_time, des = item
        print("{:<10} {:<20} {:<20} {:<20} {:<20}".format(task, ''.join(map(str, date)), ''.join(
            map(str, start_time)), ''.join(map(str, end_time)), ''.join(map(str, des))))
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


#epoch time convertion
def epoch_time(date, stime, etime):
    Y, M, d = date.split("-")
    h, m= stime.split(":")
    h1, m1= etime.split(":")
    epoch_time = datetime.datetime(int(Y), int(M), int(d), int(h), int(m)).timestamp()
    epoch_time1 = datetime.datetime(int(Y), int(M), int(d), int(h1), int(m1)).timestamp()
    return epoch_time, epoch_time1


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
        elif menu == "8":
            import time

            epoch_time = 1586944173.957986
            local_time = time.ctime(epoch_time)

            print("The local time is:", local_time)
        elif menu == "9":
            print("Logging out … ")
            time.sleep(3)
            print("Logout successful!")
        else:
            print("Invalid choice")
        menu = input("Enter your choice: ")
    thanks()
