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

def add_lists(l1, l2):
    l1 = reverse_list(l1)
    l2 = reverse_list(l2)
    carry = 0
    dummy = Node(0)
    current = dummy
    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.data
            l1 = l1.next
        if l2:
            val += l2.data
            l2 = l2.next
        carry = val // 10
        current.next = Node(val % 10)
        current = current.next
    return reverse_list(dummy.next)

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("NULL")

# Example
list1 = Node(5)
list1.next = Node(6)
list1.next.next = Node(3)

list2 = Node(8)
list2.next = Node(4)
list2.next.next = Node(2)

result = add_lists(list1, list2)
print_list(result)
