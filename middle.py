class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print("Middle element:", slow.data)

# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print_middle(head)
