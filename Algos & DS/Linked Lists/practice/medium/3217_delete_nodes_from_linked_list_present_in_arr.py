from typing import List, Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class SolutionAttept:
  def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    st = set(nums)
    prev, nxt  = None, None
    
    
    while curr:
      if curr.val in st:
        if prev == None and curr.next != None:
          nxt = curr.next
          head = head.next
          curr.next = None
          prev = curr
        elif curr.next == None:
          prev.next = None
          return head
        else:
          nxt = curr.next
          curr.next = None
          prev.next = nxt
    return head

class Solution:
  def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    delete_set = set(nums)
    dummy = ListNode[0]
    dummy.next = head
    curr = dummy
    
    while curr.next:
      if curr.next.val in delete_set:
        curr.next = curr.next.next
      else:
        curr = curr.next
    return dummy.next
          
# if starting node: - no prev
#   next = curr.next
#   curr.next = None
# if ending node: - no next
#   prev.next = None
#   break
          
# 1 -> 2 -> 3 -> 4 -> 5
# p    c    n 