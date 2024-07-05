from typing import Optional

class ListNode:
  def __init__(self, next: None, val=0) -> None:
    self.next = next
    self.val = val
    pass


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
      curr = head.next # Skip initial zero
      dummy = ListNode(0) # dummy node to start the result linked list
      res_tail = dummy
      curr_sum = 0
      
      while curr:
        if curr.val == 0: # When encountering a zero, add the sum to the result list
          res_tail.next = ListNode(curr_sum)
          res_tail = res_tail.next
          curr_sum = 0 # Reset sum
        else: # Accumulate the values between zeroes
          c += curr.val
        curr = curr.next
      return dummy.next # Return the head of the new linked list, skipping the initial node
      
  
  
# Construct the linked list: 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0
head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
s = Solution()
result = s.mergeNodes(head)

# Print the resulting linked list
while result:
    print(result.val, end=" -> ")
    result = result.next