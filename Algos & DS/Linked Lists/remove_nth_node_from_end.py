class ListNode(object):
  def __init__(self, val=0, next=None) -> None:
    self.val = val
    self.next = next
    
def removeNthFromEnd(head, n):
  dummy = ListNode(0, head)
  left = dummy
  right = head
  
  # Set R at starting distance of n+1 from L to R 
  # since L starts at dummy node
  while n > 0 and right:
    right = right.next
    n -= 1
  
  while right:
    left = left.next
    right = right.next

  # Remove nth node 
  left.next = left.next.next
  
  return dummy.next
    