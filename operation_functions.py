from printing_functions import thanks
todo_list=[]

#handle the operation of the program
def operation(operation_type, operation_value, operation_list):
    if operation_type == "add":
        #add new task with date, time and status
        operation_list.append(["", "", "", ""])
        operation_list[-1][0]=operation_value
        operation_list[-1][1]=input("Enter the date: ")
        operation_list[-1][2]=input("Enter the time: ")
        operation_list[-1][3]=input("Enter the status: ")
    elif operation_type == "update":
        #update task with date, time and status
        operation_list[operation_value[0]][0]=operation_value[1]
        operation_list[operation_value[0]][1]=input("Enter the date: ")
        operation_list[operation_value[0]][2]=input("Enter the time: ")
        operation_list[operation_value[0]][3]=input("Enter the status: ")
    elif operation_type == "delete":
        #delete task
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
    menu=input("Enter your choice: ")
    while menu != "7":
        if menu == "1":
            task=input("Enter a new task: ")
            operation("add", task, todo_list)
        elif menu == "2":
            task_index=int(input("Enter the index of the task you want to update: "))
            task=input("Enter the new task: ")
            operation("update", [task_index, task], todo_list)
        elif menu == "3":
            task_index=int(input("Enter the index of the task you want to delete: "))
            operation("delete", task_index, todo_list)
        elif menu == "4":
            operation("view", None, todo_list)
        elif menu == "5":
            operation("save", None, todo_list)
        elif menu == "6":
            task=input("Enter the task you want to search: ")
            operation("search", task, todo_list)
        else:
            print("Invalid choice")
        menu=input("Enter your choice: ")
    thanks()
