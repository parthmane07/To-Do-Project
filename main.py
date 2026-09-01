tasks = []

choice = 0

def show_tasks():
    no = 1
    for i in tasks:
        print(no,".", i["title"])
        no += 1

def add_task():
    print("'Add Task' selected")
    title = input("Enter task title:")
    for i in tasks:
        if i["title"] == title:
            print("This task already exists...")
            break
    else:
        task ={
            "title": title,
            "completed": False
        }
        tasks.append(task)

def view_tasks():
    print("'View Tasks' selected")
    if tasks == []:
        print("No tasks found.")
    j = 1
    for i in tasks:
        if i["completed"] == True:
            print(j,".", i["title"] + "-- completed")
        else:
            print(j,".",i["title"] + "-- incomplete")
    j += 1

def mark_task_as_completed():
    print("'Mark Task as Completed' selected")
    found = False
    if tasks != []:
        show_tasks()
        completed_task_number = int(input("Select completed task number:"))
        j = 1
        for i in tasks:
            if j == completed_task_number:
                found = True
                i["completed"] = True
                print("Task marked as completed...")
            j += 1
        if not found:
            print("Task not found.")
    else:
        print("No tasks added...")

def delete_task():
    print("'Delete Task' selected")
    found = False
    if tasks != []: 
        show_tasks() 
        task_to_delete = int(input("Select task number to delete:"))
        j = 1
        for i in tasks:
            if j == task_to_delete:
                found = True
                tasks.remove(i)
                print("Task deleted...")
            j += 1
        if not found:
            print("Task not found.")
    else:
        print("No tasks added...")

while choice != 5:
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice no:"))
    
        if choice == 1:
            add_task()

        elif choice == 2:
            view_tasks()
                
        elif choice == 3:
            mark_task_as_completed()

        elif choice == 4:
            delete_task()
    
        elif choice == 5:
            print("DONE, Complete your tasks as soon as possible...")

        else:
            print("Invalid choice")

    except ValueError:
            print("Invalid choice")
