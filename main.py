tasks = []

choice = 0

def show_tasks():
    for i in tasks:
        print(i["title"])

def add_task():
    print("'Add Task' selected")
    title = input("Enter task title:")
    task ={
        "title": title,
        "completed": False
    }
    tasks.append(task)

def view_task():
    print("'View Tasks' selected")
    if tasks == []:
        print("No tasks found.")
    for i in tasks:
        if i["completed"] == True:
            print(i["title"] + "-- completed")
        else:
            print(i["title"] + "-- incomplete")

def mark_task_as_completed():
    print("'Mark Task as Completed' selected")
    found = False
    show_tasks()
    completed_task_title = input("Select completed task:")
    for i in tasks:
        if i["title"] == completed_task_title:
            found = True
            i["completed"] = True
    if not found:
        print("Task not found.")

def delete_task():
    print("'Delete Task' selected")
    found = False
    show_tasks()  
    task_to_delete = input("Select task to delete:")
    for i in tasks:
        if i["title"] == task_to_delete:
            found = True
            tasks.remove(i)
    if not found:
        print("Task not found.")

while choice != 5:
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    choice = int(input("Enter your choice no:"))
    
    if choice == 1:
        add_task()

    elif choice == 2:
        view_task()
                
    elif choice == 3:
        mark_task_as_completed()

    elif choice == 4:
        delete_task()
    
    elif choice == 5:
        print("DONE, Complete your tasks as soon as possible...")

    else:
        print("Invalid choice")
