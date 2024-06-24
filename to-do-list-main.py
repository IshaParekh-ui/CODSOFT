def add_task():
    task = input("\nEnter your task: ")
    tasks.append(task)
    print("Task added\n")


def view_tasks():
    print("\n==== To Do List ====")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("\n")


def mark_completed():
    task_index = int(input("\nEnter the number of the task to mark complete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number!")
        return
    completed_task = tasks.pop(task_index)
    completed_task += "✅"
    tasks.insert(task_index, completed_task)
    print(f"Task '{completed_task}' marked complete!\n")


def delete_tasks():
    task_index = int(input("\nEnter the task number to be deleted: "))-1
    deleted_task = tasks.pop(task_index)
    print(f"Task {deleted_task} deleted!\n")


tasks = []
while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark complete")
    print("4. Delete tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_tasks()
    elif choice == '5':
        print("Exiting to-do list.")
        break
    else:
        print("Invalid choice.")