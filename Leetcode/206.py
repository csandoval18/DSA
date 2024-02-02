class Solution(object):
    def reverseList(self, head):
      c = head
      p = None
      
      while c is not None:
        n = c.next
        c.next = p
        p = c
        c = n
      return p
      
      
        
        
        