import json

tasks = []
nextID = 1


def loadTasks():
    global nextID

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

            tasks.clear()
            tasks.extend(data)

        if tasks:
            nextID = max(task["id"] for task in tasks) + 1
        else:
            nextID = 1

    except FileNotFoundError:
        tasks.clear()
        nextID = 1


def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def addTask(name):
    global nextID

    task = {
        "id": nextID,
        "name": name,
        "status": "Pending"
    }

    tasks.append(task)
    nextID += 1

    saveTasks()
    print("Task added successfully!")


def showTasks():
    if not tasks:
        print("Task list is empty!")
        return

    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Name: {task['name']}")
        print(f"Status: {task['status']}")
        print("-" * 30)


def findTask(taskID):
    for task in tasks:
        if task["id"] == taskID:
            return task

    return None


def updateTask(taskID, taskName):
    task = findTask(taskID)

    if task:
        task["name"] = taskName
        saveTasks()
        print("Task updated successfully!")
    else:
        print("Task not found!")


def removeTask(taskID):
    task = findTask(taskID)

    if task:
        tasks.remove(task)
        saveTasks()
        print("Task removed successfully!")
    else:
        print("Task not found!")
