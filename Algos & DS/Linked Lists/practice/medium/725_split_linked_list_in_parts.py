from typing import List, Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
        
class Solution:
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    # Step 1: Count the total number of nodes
    n = 0
    curr = head
    while curr:
      n += 1
      curr = curr.next
    
    # Step 2: Calculate the size of each part
    part_size = n // k # min size of each part
    extra_nodes = n % k # number of parts that will have an extra node
    
    # Step 3: Split the list
    res = []
    curr = head
    for i in range(k):
      part_head = curr
      size = part_size + (1 if i < extra_nodes else 0) # First 'extra_nodes' parts have 1 extra node
      for j in range(size - 1): # Move 'size-1' times to find the end of this part
        if curr:
          curr = curr.next
      
      if curr: # Break the link to the next part
        next_part = curr.next
        curr.next = None
        curr = next_part
      res.append(part_head)
      
    return res

class Solution:
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    n = 0
    curr = head
    while curr:
      n += 1
      curr = curr.next
    
    part_size = n // k
    extra_nodes = n % k
    res = []
    curr = head
    
    for i in range(k):
      part_head = curr
      size = part_size + (1 if i < extra_nodes else 0)
      for j in range(size-1):
        if curr:
          curr = curr.next
      if curr:
        next_part = curr.next
        curr.next = None
        