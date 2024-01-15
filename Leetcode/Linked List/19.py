from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None) -> None:
    self.val = val
    self.next = None
    
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
  dummy = ListNode(0, head)
  l, r = dummy, head
  
  while r and n>0:
    r = r.next
    n -= 1
  while r:
    l = l.next
    r = r.next
  
  l.next = l.next.next
  return dummy.next