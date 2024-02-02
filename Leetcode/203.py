class Solution(object):
  def removeElements(self, head, val):
    # Handle cases where the target value is at the beginning of the list
    while head and head.val == val:
      head = head.next
    
    # Remove target value from the remaining list
    current = head
    
    while current and current.next:
      if current.next.val == val:
        current.next = current.next.next
      else:
        current = current.next
    
    return head