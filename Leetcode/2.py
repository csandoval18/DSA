class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    tmp = ListNode(0)
    res = tmp
    remainder = 0
    
    while l1 != None or l2 != None or remainder != 0:
      if not l1 and l2:
        s = l2.val
        l2 = l2.next
          
      elif not l2 and l1:
        s = l1.val
        l1 = l1.next
        
      elif l1 and l2:
        s = l1.val + l2.val
        l1 = l1.next
        l2 = l2.next
      elif not l1 and not l2:
        s = remainder
        remainder = 0

      if remainder > 0:
        s += remainder
        remainder = 0
          
      if s > 9:
        remainder = (s) // 10
        node = ListNode(s % 10)
      else:
        node = ListNode(s)
          
      tmp.next = node
      tmp = tmp.next
    return res.next
  
# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = ListNode(2)
tmp = ListNode(4) 
l1.next = tmp 
tmp = ListNode(3)
l1.next.next = tmp 

l2 = ListNode(5)
tmp = ListNode(6)
l2.next = tmp
tmp = ListNode(4)
l2.next.next = tmp 

sol = Solution()
sol.addTwoNumbers(l1,l2)