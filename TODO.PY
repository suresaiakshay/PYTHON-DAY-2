# todo.py - A simple console-based To-Do List Application

def load_tasks(filename="todo.txt"):
    """Load tasks from a text file"""
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="todo.txt"):
    """Save tasks to a text file"""
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def view_tasks(tasks):
    """Display all tasks with numbering"""
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list"""
    task = input("\nEnter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

def remove_task(tasks):
    """Remove a task from the list"""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from your to-do list.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main program loop"""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Your to-do list has been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()