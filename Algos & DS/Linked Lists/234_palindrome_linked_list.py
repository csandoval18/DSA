from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None) -> None:
    self.val = val
    self.next = next
    
def isPalindrome(head: Optional[ListNode]) -> bool:
  slow = fast = head
  
  # Set pointers at the middle and end of linked list
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  
  # Reverse the second half of the linked list
  prev = nxt = None
  while slow:
    nxt = slow.next
    slow.next = prev
    prev = slow
    slow = nxt 
  
  # Compare both partitions
  while prev:
    if prev.val != head.val:
      return False
    prev = prev.next
    head = head.next
  return True