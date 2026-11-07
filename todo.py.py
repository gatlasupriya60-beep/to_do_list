
# To-Do List Application
# Python Developer Internship - Task 2

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file if line.strip()]
        return tasks

    except FileNotFoundError:
        return []


# Function to save tasks into file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Function to add a task
def add_task(tasks):
    task = input("Enter your task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n====== YOUR TO-DO LIST ======")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print("Removed task:", removed_task)
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number.")


# Main application
def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_task(tasks)

        elif choice == '2':
            view_tasks(tasks)

        elif choice == '3':
            remove_task(tasks)

        elif choice == '4':
            print("Thank you for using To-Do List App!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")


# Run the application
if __name__ == "__main__":
    main()
