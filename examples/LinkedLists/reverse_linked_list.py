# null  1 -> 2 -> 3
# p     c    
# n      

# null  1 -> 2 -> 3
# p     c    
#            n 

# null <- 1    2 -> 3
# p       c    
# c.next       n 

# null <- 1    2 -> 3
#         c    
# c.next  p    n 

# null <- 1    2 -> 3
#              c
# c.next  p    n 

def reverseList(head):
  p, n = None, None
  c = head
  
  while c != None:
    n = c.next
    c.next = p
    p = curr
    curr = n
  
  return head
    