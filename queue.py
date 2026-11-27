queue = []


def enqueue(task):
    queue.append(task)
    print("Task added to queue successfully!")


def dequeue():
    if not queue:
        print("Queue is empty!")
        return

    task = queue.pop(0)
    print(f"Task completed: {task['name']}")


def showQueue():
    if not queue:
        print("Queue is empty!")
        return

    for task in queue:
        print(f"ID: {task['id']}")
        print(f"Name: {task['name']}")
        print(f"Status: {task['status']}")
        print("-" * 30)
