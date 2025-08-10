def add_task():
    while True:
        task=input("Enter to-do task, 'd' to stop adding: ")
        if not task.strip():
            raise ValueError("Input cannot be empty.")
        tasks.append(task)
        tasks.append({"task": task, "done": False})
        if back_button():
            return