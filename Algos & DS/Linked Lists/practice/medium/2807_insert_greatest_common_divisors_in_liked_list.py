import math
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# Function to compute the GCD using Euclid's algorithm
def gcd(a: int, b: int) -> int:
  while b != 0:
    a, b = b, a % b
  return a
  
# 18 -> 6 -> 10 -> 3 | 18 -> (6) -> 6 -> (2) -> 10 -> (1) -> 3
  
# a = 18, b = 6
# 0-1: 18, 6 = 6, 0

# 1-2: 6, 10 = 10, 6
#      10, 6 = 6, 4
#      6, 4 = 4, 2
#      4, 2 = 2, 0

# 2-3: 10, 3 = 3, 1
#      3, 1 = 1, 0


class Solution:
  def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head 
    
    while curr and curr.next:
      gcd_val = math.gcd(curr.val, curr.next.val) # Find the GCD of the current node and the next node
      gcd_node = ListNode(gcd_val) # Create a new node with the GCD value
      
      # Insert new node between current and current.next
      gcd_node.next  = curr.next
      curr.next = gcd_node
      
      # Move to the next pair of nodes
      curr = gcd_node.next
      
    return head