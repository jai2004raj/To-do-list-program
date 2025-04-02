import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {"task": task, "completed": False}
    save_tasks(tasks)
    print(f"Task added: {task}")

def update_task(tasks, task_id, new_task):
    if task_id in tasks:
        tasks[task_id]["task"] = new_task
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Task ID not found.")

def mark_complete(tasks, task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete.")
    else:
        print("Task ID not found.")

def delete_task(tasks, task_id):
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Task ID not found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, details in tasks.items():
            status = "Done" if details["completed"] else "Pending"
            print(f"{task_id}: {details['task']} - [{status}]")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. View Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            task_id = input("Enter task ID to update: ")
            new_task = input("Enter new task description: ")
            update_task(tasks, task_id, new_task)
        elif choice == "3":
            task_id = input("Enter task ID to mark complete: ")
            mark_complete(tasks, task_id)
        elif choice == "4":
            task_id = input("Enter task ID to delete: ")
            delete_task(tasks, task_id)
        elif choice == "5":
            view_tasks(tasks)
        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
