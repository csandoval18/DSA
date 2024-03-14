from typing import List, Optional

# I solved this problem wrong because the problem does not ask to look for elements that add up to 0 such as i = 3 j = -3,
# We are looking for the sum of elements that add up to 0. Therefore we need to keep track of the prefix sum and compare to the current


class ListNode:
  def __init__(self, val=0, next=None) -> None:
    self.val = val
    self.next = next
    
    
def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
  # Turn linked list to a list
  nums = []
  while head:
    nums.append(head.val)
    head = head.next
    
  hm = {}
  i = 0
  
  while i < len(nums):
    if -nums[i] in hm:
      # If the negation of the current number is in the set, remove both numbers
      i1 = hm[-nums[i]]
      i2 = i

      # Remove the second number first to avoid affecting the index of the first number
      nums.pop(i2)
      nums.pop(i1)
      
      # Reset the set and the index to start over
      hm = {}
      i = 0
      continue  # Restart the loop since the list and set are modified
    else:
        hm[nums[i]] = i # Add the current number to the set
    i += 1
  
  return convertArrtoLinkedList(nums)
  
  
# Logic
# 1 -> 2 -> -3 -> 3 -> 1 -> None
#                      p    c
def convertArrtoLinkedList(arr: List[int]) -> Optional[ListNode]:
  n = len(arr)
  curr = None
  
  for i in range(n-1,-1,-1):
    prev = ListNode(arr[i], curr)
    curr = prev
  
  return prev


def printLinkedList(head: Optional[ListNode]):
  while head:
    if head.next != None:
      print(head.val, end=" -> ")
    else:
      print(head.val)
    
    head = head.next
  
  
arr = [1,2,-3,3,1]
head = convertArrtoLinkedList(arr)
printLinkedList(head)
res = removeZeroSumSublists(head)
printLinkedList(res)


# Working solution
def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
  dummy = ListNode(0)
  dummy.next = head
  prefix_sum = 0
  prefix_sum_map = {0: dummy}

  while head:
    prefix_sum += head.val
    prefix_sum_map[prefix_sum] = head
    head = head.next

  head = dummy
  prefix_sum = 0
  while head:
    prefix_sum += head.val
    if prefix_sum in prefix_sum_map:
      head.next = prefix_sum_map[prefix_sum].next
    head = head.next

  return dummy.next