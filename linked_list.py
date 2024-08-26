# This is a doublly Linked_list


class Node:
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class DoubllyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node()
        new_node.data = data
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def insert_after(self, prev_node_data, data):
        new_node = Node()
        new_node.data = data
        current = self.head
        while current is not None and current.data != prev_node_data:
            current = current.next_node
        if current is None:
            print(f"Node with data {prev_node_data} not found!")
        else:
            new_node.next_node = current.next_node
            new_node.prev_node = current
            current.next_node = new_node
            print(
                f"{data} has successfully been placed between {new_node.prev_node.data} and {new_node.next_node.data}"
            )

    def insert_before(self, next_node_data, data):
        new_node = Node()
        new_node.data = data
        current = self.head
        while current is not None and current.data != next_node_data:
            current = current.next_node
        if current is None:
            print(f"Node with data {next_node_data} not found!")
        else:
            new_node.prev_node = current.prev_node
            current.prev_node.next_node = new_node
            new_node.next_node = current
            current.prev_node = new_node
            print(
                f"{data} is successfully placed between {new_node.prev_node.data} and {current.data}"
            )

    def delete_head(self):
        temp = self.head
        if temp is not None:
            current = temp.next_node
            current.prev_node = None
            self.head = current
            print(f"{current.data} is now the head!")

    def delete_tail(self):
        temp = self.tail
        if temp is not None:
            current = temp.prev_node
            current.next_node = None
            self.tail = current
            print(f"{current.data} is now the tail!")

    def search_and_delete(self, data):
        current = self.head
        while current.data != data:
            current = current.next_node
        if current is None:
            print(f"Node with data {data} not found!")
        else:
            if current.data == self.head.data:
                print("Use delete_head method")
            elif current.data == self.tail.data:
                print("Use delete_tail method")
            else:
                prev_node = current.prev_node
                next_node = current.next_node
                prev_node.next_node = next_node
                next_node.prev_node = prev_node

    def search(self, data):
        current = self.head
        while current is not None and current.data != data:
            current = current.next_node
        if current is not None:
            print(f"A node contain the data {data}!")
        else:
            print(f"Node with value {data} not found!")

    def traverse_forward(self):
        current = self.head
        if current is not None:
            print("The nodes are:", end=" ")
        while current is not None:
            print(f"{current.data}", end=" ")
            current = current.next_node

    def traverse_backward(self):
        current = self.tail
        if current is not None:
            print(f"Traversing backward is:", end=" ")
        while current is not None:
            print(f"{current.data}", end=" ")
            current = current.prev_node
