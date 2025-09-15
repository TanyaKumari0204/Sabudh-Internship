class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def add_one(head):
    head = reverse_list(head)
    carry = 1
    current = head
    while current:
        total = current.data + carry
        carry = total // 10
        current.data = total % 10
        if not current.next and carry:
            current.next = Node(carry)
            break
        current = current.next
    return reverse_list(head)

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("NULL")

# Example
head = Node(1)
head.next = Node(9)
head.next.next = Node(9)
head.next.next.next = Node(9)
head = add_one(head)
print_list(head)
