# null  1 -> 2 -> 3
# p     c    
# n      

# null  1 -> 2 -> 3
# p     c    
#            n 

# null <- 1    2 -> 3
# p       c    
# c.next       n 

# null <- 1    2 -> 3
#         c    
# c.next  p    n 

# null <- 1    2 -> 3
#              c
# c.next  p    n 


from typing import List, Optional, Union


class ListNode:
  def __init__(self, val=0, next=None) -> None:
    self.next = next
    self.val = val
    pass


class Solution:
  def reverseList(self, head: Optional[ListNode]):
    c, p = head, None
    
    while c.next:
      n = c.next
      c.next = p
      p = c
      c = n
    
    return p

def array_to_linked_list(arr: List[int]):
  head = ListNode(arr[0])
  c = head
  
  for num in arr[1:]:
    c.next = ListNode(num)
    c = c.next
    
  return head
  
def print_linked_list(head: Optional[ListNode]):
  c = head
  while c.next:
    print(c.val, "-> ", end="")
    c = c.next
  print(c.val)
  
arr = [1,2,3,4,5]
head = array_to_linked_list(arr)
s = Solution()
rev_head = s.reverseList(head)
print_linked_list(rev_head)