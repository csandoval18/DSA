from typing import List, Optional

class ListNode:
  def __init__(self, val=0, next=None) -> None:
    self.val = val
    self.next = next
    
def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
  nums = []
  while head:
    nums.append(head.val)
  
  return nums
  
  
# Logic
# 1 -> 2 -> -3 -> 3 -> 1 -> None
#                      p    c
def convertArrtoLinkedList(arr: List[int]):
  n = len(arr)
  curr = None
  
  for i in range(n-1,-1,-1):
    prev = ListNode(arr[i], curr)
    curr = prev
  
  return prev

def printLinkedList(head: Optional[ListNode]):
  while head:
    print(head.val, end=" -> ")
    head = head.next
  
  
arr = [1,2,-3,3,1]
head = convertArrtoLinkedList(arr)
printLinkedList(head)

