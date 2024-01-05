class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None
    
def divideList1(head: Node) -> Node: 
  def traverse(l: Node, r: Node) -> Node:
    res = l
    
    while r.next:
      l.next = r.next
      l = r.next
      r = l.next
    return res
  
  res1 = traverse(head, head.next)
  res2 = traverse(head.next, head.next.next)

  return res1, res2
  

def divideList(head: Node) -> [Node or None]:
  if not head:
    return [None, None]
  
  h1, h2 = head, head.next
  
  if not h1 or not h2:
    return [head, None]
  
  l, r = h1, h2
  while l and r:
    # Update next pointers to divide linked list
    l.next = r.next
    # Here we make sure the next of the updated left.next actually exists, if it does
    # then we set the right.next pointer to left.next's next = left.next.next
    if l.next:
      r.next = l.next.next
    
    r = r.next
    l = l.next
  return [h1, h2]

n1 = Node(1)  
n2 = Node(2)  
n3 = Node(3)  
n4 = Node(4)  
n5 = Node(5)  

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

res = divideList(n1)
l1 = res[0]
l2 = res[1]
while l1:
  if l1.next:
    print(l1.data, end="->")
  else:
    print(l1.data)
  l1 = l1.next
  
while l2:
  if l2.next:
    print(l2.data, end="->")
  else:
    print(l2.data)
  l2 = l2.next