class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  
# [1,2,3,4,5]
# n = 2
# 1 -> 2 -> 3 -> 4 -> 5
# ans:
# 1 -> 2 -> 3 -> 5
def removeNthFromEnd(head, n):
  # 1. Traverse through list first to get length
  # 2. len(linkedlist) - n = index of node to remove
  node = head
  listLen = 0
  
  while node:
    listLen += 1
    node = node.next
  
  node = head
  
  
  
  


# Create test arr for ans 
head = ListNode(1)
node = head
for i in range(1,5): 
  node.next = ListNode(i+1)
  node = node.next

node = head
ll_arr = []

while node:
  ll_arr.append(node.val)
  node = node.next

print(ll_arr)
  
