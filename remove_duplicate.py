class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("NULL")

# Example
head = Node(10)
head.next = Node(15)
head.next.next = Node(15)
head.next.next.next = Node(20)
head.next.next.next.next = Node(20)
head = remove_duplicates(head)
print_list(head)
