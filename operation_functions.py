from printing_functions import thanks, main_menu
import datetime
import time

#declaring a empty list
todo_list = []

# adition to list
def add_to_list(description,start_epoch_time, end_epoch_time, address):
    
    todo_list.append(["","","",""])
    todo_list[-1][0]=description
    todo_list[-1][1]=start_epoch_time
    todo_list[-1][2]=end_epoch_time
    todo_list[-1][3]=address
    print("\nTask added successfully!\n")

def add_task():
    description = input("Enter a new task: ")
    
    date= input("Enter a date in YYYY-MM-DD format: ")
    s_time= input("Enter a Start time in HH:MM format(24 hr): ")
    e_time= input("Enter the End time in HH:MM format(24 hr): ")
    address= input("Enter the address: ")
    try:
        start_epoch_time, end_epoch_time = epoch_time(date, s_time, e_time)
    except:
        print("Invalid date or time format")
        main_menu()
        user_input()
    if (start_epoch_time > end_epoch_time):
        print("Start time should be less than end time")
        # todo_list.pop(-1)
    else:
        if todo_list:
            for index, task in enumerate(todo_list):
                if task[1]<=start_epoch_time and task[2]>=end_epoch_time:
                    #converting the time to string
                    date, start_time, end_time = epoch_time_toString(task[1], task[2])
                    print("Opps! Task overlaps with another task")
                    print ("Have a look at the following task:")
                    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
                        "Description","Date", "Start time", "End time", "Address"))
                    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
                        task[0], date,start_time, end_time, task[3]))
            else:
                add_to_list(description, start_epoch_time, end_epoch_time, address)
                        
        else:
            add_to_list(description, start_epoch_time, end_epoch_time, address)
    main_menu()
    user_input()


def update_task():
    if todo_list:
        task_or_date = input("Enter a task or date: ")
        # search in list and print index
        try:
            for index, task in enumerate(todo_list):
                if task[0] == task_or_date or task[1] == task_or_date:
                    description = input("Enter a new task: ")
                    date= input("Enter a date in YYYY-MM-DD format: ")
                    s_time= input("Enter a Start time in HH:MM format(24 hr): ")
                    e_time= input("Enter the End time in HH:MM format(24 hr): ")
                    address= input("Enter the address: ")
                    try:
                        start_epoch_time, end_epoch_time = epoch_time(date, s_time, e_time)
                    except:
                        print("Invalid date or time format")
                        main_menu()
                        user_input()
                    if (start_epoch_time > end_epoch_time):
                        print("Start time should be less than end time")
                        # todo_list.pop(-1)
                    else:
                        # update the task
                        todo_list[index][0] =description
                        todo_list[index][1] = start_epoch_time
                        todo_list[index][2] = end_epoch_time
                        todo_list[index][3] = address
                        print("\nTask Updated successfully!")
            main_menu()
            user_input()
        except:
            print("Task not found")
            main_menu()
            user_input()
            
    else:
        print("No tasks to update")
        main_menu()
        user_input()
    


def delete_task():
    if todo_list:

        try:
            task_or_date = input("Enter a task or date: ")
            # search in list and print index
            for index, task in enumerate(todo_list):
                if task[0] == task_or_date or task[1] == task_or_date:
                    # delete the task
                    todo_list.pop(index)
                    print("\nTask deleted successfully!")
            main_menu()
            user_input()
        except:
            print("Task not found")
            main_menu()
            user_input()
    else:
        print("No tasks to delete")
        main_menu()
        user_input()

def view_all():
    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
        'Description', 'Date', 'Start Time', 'End Time', 'Place'))
    for item in todo_list:
        des, epoch_start_time, epoch_end_time, add = item
        date, start_time, end_time = epoch_time_toString(epoch_start_time, epoch_end_time)

        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(des, date, start_time, end_time, add))
    main_menu()
    user_input()

def export():
    with open("todo.txt", "w") as file:
        file.write("{:<20} {:<20} {:<20} {:<20} {:<20}".format('Description', 'Date', 'Start Time', 'End Time', 'Place'))
        for item in todo_list:
            des, epoch_start_time, epoch_end_time, add = item
            print(item)
            print(epoch_end_time)
            date, start_time, end_time = epoch_time_toString(epoch_start_time, epoch_end_time)
            file.write("\n")
            file.write("{:<20} {:<20} {:<20} {:<20} {:<20}".format(des, date, start_time, end_time, add))
        file.write(
            "\n********************************************************************\n")
    print("File exported")
    main_menu()
    user_input()

def search():
    if todo_list:
        search_term = input("Enter a task to search: ")
        for item in todo_list:
            if search_term in item:
                date, start_time, end_time = epoch_time_toString(item[1],item[2])
                print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
                    'Description', 'Date', 'Start Time', 'End Time', 'Place'))
                print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(item[0], date, start_time, end_time, item[3]))
    else:
        print("You have no tasks assigned yet")
    main_menu()
    user_input()

#epoch to string
def epoch_time_toString(s_time, e_time):
    date= datetime.datetime.fromtimestamp(s_time).strftime("%Y-%m-%d")
    start_time = datetime.datetime.fromtimestamp(s_time).strftime("%H:%M")
    end_time = datetime.datetime.fromtimestamp(e_time).strftime("%H:%M")
    return date, start_time, end_time

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
            export()
        elif menu == "6":
            search()
        else:
            print("Invalid choice")
        menu = input("Enter your choice: ")
    thanks()
