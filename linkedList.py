class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

   
    def addHistory(self, task):
        newNode = Node(task.copy())

        if self.head is None:
            self.head = newNode
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode

  
    def showHistory(self):
        if self.head is None:
            print("Task history is empty!")
            return

        current = self.head

        while current is not None:
            print(f"ID: {current.data['id']}")
            print(f"Name: {current.data['name']}")
            print(f"Status: {current.data['status']}")
            print("-" * 30)

            current = current.next
