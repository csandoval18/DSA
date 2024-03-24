class ListNode:
  def __init__(self, val=0, next=None) -> None:
    self.val = val
    self.next = next
  
def reorderList(head):
  if not head or not head.next:
    return head
  
  # Step 1: Find the middle of the list
  slow = head
  fast = head.next
  while fast and fast.next:
    slow = head.next
    fast = head.next.next
  
  # Split the list into two halves
  second_half = slow.next
  slow.next = None
  
  # Step 2: Reverse the second half
  prev = None
  curr = second_half
  
  while curr:
    tmp = curr.next
    curr.next = prev
    prev = curr
    curr = tmp
  
  # Merge the two halves
  start = head
  second = prev
  while second:
    tmp1 = start.next
    tmp2 = second.next
    start.next = second
    second.next = tmp1
    start = tmp1
    second = tmp2
    
  return head