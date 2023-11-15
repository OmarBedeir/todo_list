def add_task(todo_list):
    # Prompt the user to enter a task
    task = input("Enter a task: ")
    # Add the task to the todo_list
    todo_list.append(task)
    # Print a message indicating that the task has been added
    print("Task added.")

def view_tasks(todo_list):
    # Check if the todo_list is empty
    if not todo_list:
        # Print a message if there are no tasks to display
        print("No tasks to display.")
    else:
        # Iterate through the tasks in the todo_list and print each task
        for task in todo_list:
            print(task)

def remove_task(todo_list):
    # Check if the todo_list is empty
    if not todo_list:
        # Print a message if there are no tasks to remove
        print("No tasks to remove.")
    else:
        # Prompt the user to enter a task to remove
        task = input("Enter a task: ")
        # Check if the entered task is in the todo_list
        if task in todo_list:
            # Remove the task from the todo_list
            todo_list.remove(task)
            # Print a message indicating that the task has been removed
            print("Task removed.")
        else:
            # Print a message if the entered task is not found in the todo_list
            print("Task not found.")

# Initialize an empty todo_list
todo_list = []

while True:
    # Prompt the user to enter a command (add, view, remove, exit)
    user_action = input("Enter a command (add, view, remove, exit): ")

    # Check the user's command and call the corresponding function
    if user_action == "add":
        add_task(todo_list)
    elif user_action == "view":
        view_tasks(todo_list)
    elif user_action == "remove":
        remove_task(todo_list)
    elif user_action == "exit":
        # Exit the while loop if the user enters "exit"
        break
    else:
        # Print a message for an invalid command
        print("Invalid command.")

        print("Invalid command")
