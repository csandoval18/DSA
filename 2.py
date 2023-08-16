class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    tmp = ListNode(0)
    res = tmp.next
    remainder = 0
    
    while l1 != None or l2 != None:
      if remainder > 0:
        s = l1.val + l2.val + remainder
        remainder = 0
      else:
        s = l1.val + l2.val
        
      if s > 9:
        remainder = (s) // 10
        node = ListNode(s % 10)
      else:
        node = ListNode(s)
        
      tmp.next = node
      l1 = l1.next
      l2 = l2.next
        
      tmp = tmp.next
      print(tmp.val)
        
    return res
  
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