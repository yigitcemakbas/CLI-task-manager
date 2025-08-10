import os
import json

tasks=[]

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def add_task():
    print("Enter 'd' when done adding, 'b' to go back.")
    while True:
        task=input("Enter to-do task: ")
        if task.lower()=='b':
            print("Going back...")
            return
        if task.lower()=='d':
            clear_screen()
            print("===TO-DO LIST===")
            list_tasks()
            input("Press Enter to return to menu.")
            break
        if not task.strip():
            input("Input cannot be empty. 'b' to go back.")
            continue
        tasks.append({"task": task, "done": False})
    
    
def remove_task():
    while True:
        clear_screen()
        print("Enter 'd' when done removing, 'b' to go back.")
        list_tasks()
        choice = input("Enter task number to remove: ")
        if choice=='b':
            print("Going back...")
            return
        if choice=='d':
            clear_screen()
            print("Done removing tasks.")
            list_tasks()
            input("Press Enter to return to menu.")
            break
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        index=int(choice)-1
        if 0<=index<len(tasks):
            removed=tasks.pop(index)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")
            input("'b' to go back: ")
    
def list_tasks():
    if not tasks:
        print("No tasks to show.")
        input("Press Enter to return to menu.")
        return
    max_len=max(len(item["task"]) for item in tasks)
    for i, item in enumerate(tasks,1):
        status="✔" if item["done"] else " "
        print(f"{i}. {item['task'].ljust(max_len)}   [{status}]")
    
def update_task():
    print("Enter 'd' when done, 'b' to go back.")
    while True:
        clear_screen()
        print("Enter 'd' when done.")
        list_tasks()
        choice = input("Enter task number to toggle status: ").strip()

        if choice.lower() == 'b':
            print("Going back...")
            return
        elif choice.lower() == 'd':
            clear_screen()
            print("Done updating task status.")
            list_tasks()
            input("Press Enter to return to menu.")
            break

        try:
            index = int(choice) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = not tasks[index]["done"]
            else:
                print("Invalid task number.")
                input("Press Enter to try again.")
        except ValueError:
            print("Please enter a valid number.")
            input("Press Enter to try again.")


def save_to_file():
    try:
        with open("TO-DO.json", "w") as f:
            json.dump(tasks,f,indent=4)
        with open("TO-DO.txt", "w") as f:
            f.write("========= TO-DO LIST =========\n")
            if tasks:
                max_len=max(len(item["task"]) for item in tasks)
                for i, item in enumerate(tasks,1):
                    status="✔" if item["done"] else " "
                    f.write(f"{i}. {item['task'].ljust(max_len)}   [{status}]\n")

        print("Tasks saved successfully.")
        input("Press Enter to return to menu.")

    except (IOError, OSError) as e:
        print(f"Error saving tasks: {e}")
    input("Press Enter to return to menu.")

def load_from_file():
    global tasks
    try:
        with open("TO-DO.json","r") as f:
            tasks=json.load(f)
        clear_screen()
        print("Tasks loaded successfully.")
        list_tasks()
        input("Press enter to return to menu.")
    except FileNotFoundError:
        print("No saved tasks found.")
        input("Press Enter to return to menu.")
    except json.JSONDecodeError:
        print("Error loading tasks. File might be corrupted.")
        input("Press Enter to return to menu.")
    except (IOError,OSError) as e:
        print(f"Erorr reading file: {e}")
        input("Press Enter to return to menu.")

def main():
    while True:
        clear_screen()
        print("\n===========Task manager===========")
        print("1. Add task.")
        print("2. Remove task.")
        print("3. Update task status.")
        print("4. View tasks.")
        print("5. Save tasks to file.")
        print("6. Load tasks from file.")
        print("7. Quit.")

        try:
            selection=int(input("Type the corresponding number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        clear_screen()
    
        if selection==1:
            add_task()
        elif selection==2:
            remove_task()
        elif selection==3:
            update_task()
        elif selection==4:
            list_tasks()
            input("Press Enter to return to menu.")
        elif selection==5:
            save_to_file()
        elif selection==6:
            load_from_file()
        elif selection==7:
            print("Exiting...")
            break
        else:
            print("Invalid selection.")
            input("Press Enter to continue...")

if __name__=="__main__":
    main()
