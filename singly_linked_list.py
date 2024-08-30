class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        self.head = new_node
        print(f"{data} has successfully been added to the list!")

    def insert_at_end(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = None
        if self.head is None:
            self.head = new_node
            print(f"{data} was successfully added to the list!")
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            print(f"{data} was successfully added to the end of list!")

    def insert_before(self, data, next_node_data):
        new_node = Node()
        new_node.data = data
        temp = self.head
        prev = None
        while temp.data != next_node_data and temp is not None:
            prev = temp
            if prev.next is not None:
                temp = prev.next
        if temp is not None:
            prev.next = new_node
            new_node.next = temp
            print(
                f"{data} has been placed between {
                    prev.data} and {temp.data}"
            )
        else:
            print(f"Node with the value {data} is not in the list.")

    def insert_after(self, data, prev_node_data):
        new_node = Node()
        new_node.data = data
        current = self.head
        while current.data != prev_node_data and current is not None:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        print(f" {data}  was successfully after {prev_node_data}")

    def delete_node(self, data):
        temp = self.head
        prev = None

        if temp is not None and temp.data == data:
            self.head = temp.next
            print(f"Node with data {data} is deleted")
        else:
            while temp is not None and temp.data != data:
                prev = temp
                temp = prev.next
            if temp is None:
                print("Key not found")
            else:
                prev.next = temp.next
                print(f"Node with the value {data} is deleted.")

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                print(f"{data} has been found!")
                return
            temp = temp.next
        if temp is None:
            print(f"{data} not found!")

    def traverse(self):
        temp = self.head
        count = 0
        while temp is not None:
            if count == 0:
                print("The value of the nodes are: ", end="")
                count += 1
            print(temp.data, end=" ")
            temp = temp.next
