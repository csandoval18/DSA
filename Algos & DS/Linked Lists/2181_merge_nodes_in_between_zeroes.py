from typing import Optional

class ListNode:
  def __init__(self, next: None, val=0) -> None:
    self.next = next
    self.val = val
    pass


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
      c = head.next # Skip initial zero
      dummy = ListNode(0) # dummy node to start the result linked list
      res_tail = dummy
      curr_sum = 0
      
      while c:
        if c.val == 0: # When encountering a zero, add the sum to the result list
          
      