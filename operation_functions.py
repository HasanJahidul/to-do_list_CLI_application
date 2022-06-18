from printing_functions import thanks
todo_list = []

# handle the operation of the program
def add_task():
    task = input("Enter a new task: ")
    todo_list.append(["", "", "", ""])
    todo_list[-1][0] = task
    todo_list[-1][1] = input("Enter the date: ")
    todo_list[-1][2] = input("Enter the time: ")
    todo_list[-1][3] = input("Enter the status: ")

def update_task():
    task_or_date = input("Enter a task or date: ")
    # search in list and print index
    for index, task in enumerate(todo_list):
        if task[0] == task_or_date or task[1] == task_or_date:
            #update the task
            todo_list[index][0] = input("Enter the Updated task: ")
            todo_list[index][1] = input("Enter the Updated date: ")
            todo_list[index][2] = input("Enter the Updated time: ")
            todo_list[index][3] = input("Enter the Updated status: ")

def delete_task():
    task_or_date = input("Enter a task or date: ")
    todo_list.pop()

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
            task_index = int(
                input("Enter the index of the task you want to delete: "))
            operation("delete", task_index, todo_list)
        elif menu == "4":
            operation("view", None, todo_list)
        elif menu == "5":
            operation("save", None, todo_list)
        elif menu == "6":
            task = input("Enter the task you want to search: ")
            operation("search", task, todo_list)
        else:
            print("Invalid choice")
        menu = input("Enter your choice: ")
    thanks()
