# To-Do List (CLI) – Simple console app using Python basics

def show_tasks(tasks):
    """Display all tasks with indexes."""
    if not tasks:
        print("\nNo tasks yet! ✅\n")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")
    print()

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task description: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added! ✅")
    else:
        print("Task cannot be empty.")

def mark_done(tasks):
    """Mark a task as done."""
    if not tasks:
        print("No tasks to mark as done.")
        return
    show_tasks(tasks)
    raw = input("Enter task number to mark done: ").strip()
    if not raw.isdigit():
        print("Invalid input.")
        return
    idx = int(raw) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        print("Task marked as done! ✔")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task."""
    if not tasks:
        print("No tasks to delete.")
        return
    show_tasks(tasks)
    raw = input("Enter task number to delete: ").strip()
    if not raw.isdigit():
        print("Invalid input.")
        return
    idx = int(raw) - 1
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please choose 1–5.")

if __name__ == "__main__":
    main()
