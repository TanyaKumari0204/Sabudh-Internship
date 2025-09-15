class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def second_last(head):
    if not head or not head.next:
        print("List too short")
        return
    while head.next and head.next.next:
        head = head.next
    print("Second last element:", head.data)

# Example
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(33)
head.next.next.next.next.next = Node(67)
second_last(head)
