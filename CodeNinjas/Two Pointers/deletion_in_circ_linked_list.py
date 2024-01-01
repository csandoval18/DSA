class Node :
  def __init__(self, data) :
    self.data = data
    self.next = None


# r   
# 1->2->3->4->5
# l  

#    r   
# 1->2->3->4->5
# l  

#       r   
# 1->2->3->4->5
#    l  

#       r   
# 1->2->3->4->5
#    l  

# This doesn't work because it is a CIRCULAR linked list therefore I need to remove all 
# occurances of the key
def deleteNodeAttempt(head, key): 
  node = head
  l, r = node, node
  
  while r:
    print(l.data, end=" ")
    print(r.data)
    if r.data == key:
      if r == head:
        return head.next
      elif r.next:
        l.next = r.next
      else:
        l.next = None
      break
    l = r
    r = r.next

  return node
  
def deleteNode(head, key):
  if not head:
    return None

  current = head
  prev = None

  # Traverse the circular linked list to find the key
  while True:
    if current.data == key:
      # Key found, adjust pointers to delete the node
      if prev is None:  # Deleting the head node
        while current.next != head:
          current = current.next
        if current == head:  # If only one node in the list
          return None
        else:
          current.next = head.next
          head = head.next
      else:
        prev.next = current.next

      break

    prev = current
    current = current.next

    if current == head:
      break  # Key not found, break to avoid an infinite loop

    return head
  
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

head  = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

res = deleteNode(head, 3)
while res:
  print(res.data)
  res = res.next