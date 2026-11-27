from tasks import *
from stack import push, undo
from queue import enqueue, dequeue, showQueue
from linkedList import LinkedList
from menu import showMenu



history = LinkedList()
loadTasks()

while True:
    showMenu()

    choice = input("Enter your choice: ")

    try:
        choice = int(choice)

        if choice == 1:
            name = input("Enter task name: ")
            addTask(name)

            if tasks:
                push("add", tasks[-1])

        elif choice == 2:
            taskID = int(input("Enter task ID: "))
            taskName = input("Enter new task name: ")

            task = findTask(taskID)

            if task:
                push("update", task)
                updateTask(taskID, taskName)
            else:
                print("Task not found!")

        elif choice == 3:
            taskID = int(input("Enter task ID: "))

            task = findTask(taskID)

            if task:
                index = tasks.index(task)
                push("remove", task, index)
                removeTask(taskID)
            else:
                print("Task not found!")

        elif choice == 4:
            showTasks()

        elif choice == 5:
            taskID = int(input("Enter task ID: "))
            task = findTask(taskID)

            if task:
                enqueue(task)
            else:
                print("Task not found!")

        elif choice == 6:
            completedTask = dequeue()

            if completedTask:
                completedTask["status"] = "Completed"
                history.addHistory(completedTask)
                saveTasks()

        elif choice == 7:
            undo(tasks)
            saveTasks()

        elif choice == 8:
            history.showHistory()

        elif choice == 9:
            showQueue()

        elif choice == 0:
            print("Program terminated.")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")
