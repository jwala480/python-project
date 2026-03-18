tasks = []

# Function to add task
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to remove task
def remove_task():
    view_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number!")
    except:
        print("Please enter a valid number!")

# Main menu function
def menu():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run the program
menu()