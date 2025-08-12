# Task definition:
# Task: name of the task
# Completed: () (x)


def adding_task(tasks, task_name):

    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' has been added")
    return

def see_tasks(tasks):
    print("\n See your current to-do list:")
    for index, task in enumerate(tasks, start =1):
        status = "✔" if task["completed"] else ""
        task_name = task["name"]
        print(f"{index}. [{status}], {task_name}")
    return

def update_task_name(tasks, task_index, task_new_name):
    task_index_adjust = int(task_index) - 1
    if task_index_adjust >= 0 and task_index_adjust < len(tasks):
        tasks[task_index_adjust]["name"] = task_new_name
        print(f"Task {task_index} renamed to {task_new_name}")
    else:
        print("\nTask chosen does not exist")
    return
    
def complete_task(tasks, task_index):
    task_index_adjust = int(task_index) - 1
    if task_index_adjust >= 0 and task_index_adjust < len(tasks):
        tasks[task_index_adjust]["completed"] = True
    print(f"Task {task_index} tagged as completed: ")
    return

def delete_task(tasks): 
    for item in tasks:
        if item["completed"] == True:
            tasks.remove(item)
    print(f"Tasks completed have been removed")
    return

tasks = []

while True:
    print("\n Menu to for managing tasks/to-do-list")
    print("1. Add a task")
    print("2. See tasks")
    print("3. Update a task")
    print("4. Mark task as completed")
    print("5. Delete completed task(s)")
    print("6. Exit")

    user_input = input("Please choose an item: ")

    if user_input == "1":
        task_name = input("Please add your task: ")
        adding_task(tasks, task_name)
    elif user_input == "2":
        see_tasks(tasks)
    elif user_input == "3":
        see_tasks(tasks)
        task_index = input("Type the number of the task you'd like to update: ")
        task_new_name = input("\nPlease rename your task: ")
        update_task_name(tasks, task_index, task_new_name)
    elif user_input == "4":
        see_tasks(tasks)
        task_index = input("Please select the task you have completed: ")
        complete_task(tasks, task_index)
    elif user_input == "5":
        see_tasks(tasks)
        delete_task(tasks)
    elif user_input == "6":
        break