# ToDoManager

A simple console-based Task Management System developed using Python. The project allows users to manage tasks and demonstrates the use of basic data structures.

## Features

- **Add Task:** Add new tasks to the task list.
- **Update Task:** Modify existing task names.
- **Remove Task:** Delete tasks by ID.
- **Show All Tasks:** Display all available tasks.
- **Queue Management:** Add tasks to a queue and complete the next task using FIFO (First In, First Out).
- **Undo:** Undo Add, Update, and Remove operations using a Stack.
- **Task History:** Store and display completed tasks using a Linked List.
- **JSON Storage:** Save tasks in a JSON file and load them when the program starts.

## Project Structure

```text
ToDoManager/
│
├── main.py
├── tasks.py
├── tasks.json
├── stack.py
├── queue.py
├── linkedList.py
├── menu.py
└── README.md
```

## Technologies Used

- Python
- JSON
- Stack
- Queue
- Linked List

## How to Run

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Open the project folder.

3. Run the program:

```bash
python main.py
```

## Task Storage

Tasks are stored in `tasks.json`.

The program automatically loads existing tasks when it starts and saves changes when tasks are added, updated, or removed.

## Menu Options

| Option | Description |
|---|---|
| 1 | Add task |
| 2 | Update task |
| 3 | Remove task |
| 4 | Show all tasks |
| 5 | Add task to queue |
| 6 | Complete next task |
| 7 | Undo |
| 8 | Task history |
| 9 | Show queue |
| 0 | Exit |

## Data Structures

- **List:** Stores and manages tasks.
- **Stack:** Supports Undo operations.
- **Queue:** Manages tasks in FIFO order.
- **Linked List:** Stores completed task history.

## Storage Note

Task data is persisted in JSON. Queue contents, Stack operations, and Linked List history are maintained in memory during program execution.