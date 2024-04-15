class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head node created: ", self.head.value)
        new_node.next = self.head
        self.head = new_node
        print("Prepended new head node with value:", self.head.value)
        print("Node following head is:", self.head.next.value)

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head node created: ", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)


llist = LinkedList()
llist.prepend("First node")
llist.prepend("Inserted new first node")
