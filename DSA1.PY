from collections import deque

# --------------------
# 1. Stack (LIFO)
# --------------------
print("\n--- Stack Operations ---")
stack = []

# Insert
stack.append(10)
stack.append(20)
print("Stack after insert:", stack)

# Delete
stack.pop()
print("Stack after delete:", stack)

# Update
if stack:
    stack[-1] = 99
print("Stack after update:", stack)

# Sort
stack.sort()
print("Stack after sort:", stack)

# --------------------
# 2. Queue (FIFO)
# --------------------
print("\n--- Queue Operations ---")
queue = deque()

# Insert
queue.append(10)
queue.append(20)
print("Queue after insert:", list(queue))

# Delete
queue.popleft()
print("Queue after delete:", list(queue))

# Update
if queue:
    queue[0] = 99
print("Queue after update:", list(queue))

# Sort
queue = deque(sorted(queue))
print("Queue after sort:", list(queue))

# --------------------
# 3. List (Dynamic Array)
# --------------------
print("\n--- List Operations ---")
lst = [5, 2, 9]

# Insert
lst.append(4)
lst.insert(1, 7)  # insert at index 1
print("List after insert:", lst)

# Delete
lst.remove(2)  # remove by value
lst.pop()      # remove last element
print("List after delete:", lst)

# Update
lst[0] = 99
print("List after update:", lst)

# Sort
lst.sort()
print("List after sort:", lst)

# --------------------
# 4. Linked List
# --------------------
print("\n--- Linked List Operations ---")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):  # Insert
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, value):  # Delete
        curr = self.head
        prev = None
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def update(self, old_value, new_value):  # Update
        curr = self.head
        while curr:
            if curr.data == old_value:
                curr.data = new_value
                return
            curr = curr.next

    def to_list(self):  # Helper to print
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# Usage
ll = LinkedList()
ll.append(5)
ll.append(10)
ll.append(15)
print("Linked List after insert:", ll.to_list())

ll.delete(10)
print("Linked List after delete:", ll.to_list())

ll.update(5, 99)
print("Linked List after update:", ll.to_list())

# Sort manually (Convert to list → sort → rebuild linked list)
data_list = sorted(ll.to_list())
ll = LinkedList()
for data in data_list:
    ll.append(data)
print("Linked List after sort:", ll.to_list())

