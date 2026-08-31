tasks = []

choice = 0

while choice != 5:
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    choice = int(input("Enter your choice no:"))
    
    if choice == 1:
        print("'Add Task' selected")

        tital = input("Enter task tital:")

        task ={
            "tital": tital,
            "completed": False
        }
        tasks.append(task)

    elif choice == 2:
        print("'View Tasks' selected")

        if tasks == []:
                    print("No tasks found.")

        for i in tasks:
            if i["completed"] == True:
                print(i["tital"] + "-- completed")
            else:
                print(i["tital"] + "-- incomplete")
                
    elif choice == 3:
        print("'Mark Task as Completed' selected")
        found = False

        for i in tasks:
            print(i["tital"])

        select_completed_task = input("Select completed task:")

        for i in tasks:
            if i["tital"] == select_completed_task:
                found = True
                i["completed"] = True

        if not found:
            print("Task not found.")

    elif choice == 4:
        print("'Delete Task' selected")
        found = False

        for i in tasks:
            print(i["tital"])

        select_task_to_delete = input("Select task to delete:")

        for i in tasks:
            if i["tital"] == select_task_to_delete:
                found = True
                tasks.remove(i)

        if not found:
            print("Task not found.")
    
    elif choice == 5:
        print("DONE, Complete your tasks as soon as possible")

    else:
        print("Invalid choice")
