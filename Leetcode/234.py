class Solution(object):
  def isPalindrome(self, head):
    curr = head
    arr = []
    
    # Get linked list length
    while curr:
      arr.append(curr.val)
      curr = curr.next
      
    l, r = 0, len(arr) - 1
    
    for i in range(len(arr) // 2):
      if arr[l] != arr[r]:
        return False
      l += 1
      r -= 1
    return True
    
    
  #  O(n) Solution O(1) space
def isPalindrome(self, head): 
  fast = head
  slow = head
  
  # Find middle (slow)
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  
  # Reverse second half of linked list
  prev = None
  while slow:
    n = slow.next
    slow.next = prev
    prev = slow
    slow = n

  l, r = head, prev
  while r:
    if l.val != r.val:
      return False
    l = l.next
    r = r.next
  return True