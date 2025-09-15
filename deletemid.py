
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_middle(head):
    if not head or not head.next:
        return None
    slow = fast = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = slow.next
    return head

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("NULL")

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = delete_middle(head)
print_list(head)
