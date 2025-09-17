# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:  # queue became empty
            self.rear = None
        return value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def print_queue(self):
        current = self.front
        if current is None:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next
    


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            served = queue.dequeue()
            if served:
                print(f"Helped: {served}")
            else:
                print("No customers to help.")

        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            next_customer = queue.peek()
            if next_customer:
                print(f"Next customer: {next_customer}")
            else:
                print("No customers in the queue.")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()
            
        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()



# design memo
# 1. Why is a stack the right choice for undo/redo?
# Choosing the right structure depended on the order in which actions or requests needed to be processed.Stacks follow the Last-in, First-out principle
# The most recent action must be the first to undo. Redoing requires retrieving the most recently undone action.

# 2. Why is a queue better suited for the help desk?
# A queue is better suited for the help desk because it follows the First-in, Last-out principle. Customers should be helped in the order they arrive.

# 3. How do your implementations differ from Python's built-in list?
# My implementations differ from Python's built-in list because I used custom Node objects connected by references. Unlike lists, these linked structures
# allowed ease for adding and removing from the front.