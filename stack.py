stack = []


def push(action, task, index=None):
    operation = {
        "action": action,
        "task": task.copy(),
        "index": index
    }

    stack.append(operation)


def undo(tasks):
    if not stack:
        print("Undo history is empty!")
        return

    lastOperation = stack.pop()

    action = lastOperation["action"]
    taskData = lastOperation["task"]

    if action == "add":
        for task in tasks:
            if task["id"] == taskData["id"]:
                tasks.remove(task)
                print("Add operation undone!")
                return

    elif action == "update":
        for task in tasks:
            if task["id"] == taskData["id"]:
                task["name"] = taskData["name"]
                task["status"] = taskData["status"]
                print("Update operation undone!")
                return

    elif action == "remove":
        index = lastOperation["index"]
        tasks.insert(index, taskData)
        print("Remove operation undone!")
        return

    print("Task not found!")
