todo_list = []
# Start the application loop
while True:
# Prompt the user to enter a command
    user_action = input("Enter your task (add, view, remove, exit): ")
# Check the user's command and call the corresponding function
    if user_action.lower() == "add":
        task = input("Enter a task: ")
        priority = input("Enter priority (high, medium, low): ")  # Added priority feature
        due_date = input("Enter due date (optional): ")  # Added due date feature
        description = input("Enter you description")
        todo_list.append({
            "task": task,
            "priority": priority,
            "due_date": due_date,
            "description": description,  # Task Description initialization
            
        })
        print("Your task added.")

    elif user_action.upper() == "VIEW":
        if not todo_list:
            print("No tasks to display.")
        else:
            for task in todo_list:
                print(f"Task: {task['task']}, Priority: {task['priority']}, Due Date: {task['due_date']}")
                print(f"Description: {task['description']}, Completed: {task['completed']}")
    
    elif user_action.lower() == "remove":
        if not todo_list:
            print("No tasks to remove.")
        else:
            task_to_remove = input("Enter a task to remove: ")
            todo_list = [task for task in todo_list if task['task'] != task_to_remove]
            print(f"Task '{task_to_remove}' removed.")
# Exit the loop if the user enters "exit"
    elif user_action.upper() == "EXIT":
        break
# Print a message for an invalid command
    else:
        print("Invalid command.")
