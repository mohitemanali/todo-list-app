tasks =[]
print("To-Do list Menu:")
print("1. Add a task")
print("2. View tasks")
print("3. Delete a task")
print("4. Exit")
while True:
    choice = input("Enter your choice (1-4):")
    if choice == "1":
        task = input("Enter the task:")
        tasks.append(task)
        print("Your Task  added successfully!")
        
    elif choice == "2":
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i,task)
            
    elif choice == "3":
        task_number = int(input("Enter number of task to be deleted:"))
        
        if 0 < task_number <= len( tasks ):
            tasks.pop(task_number - 1)
            print("your task deleted successfully")
        else:
            print("Invalid task number")
    elif choice == "4":
        print("Existing program....")
        break
    else:
        print("Invalid choice")
