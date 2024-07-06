from typing import List, Optional


# Local maxima: The current node has a value strickly greater than (>) the previous node and the next node.
# Local minima: The current node has a value strickly smaller than (<) the previous node and the next node.

# Return an array of len 2 containing [minDistance, maxDistance]  
# maxDistance: The max distance between any two distinct critical points
# minDistance: The min distance vetween any two distinct cirtical points.
# If there are fewer than two critical points return [-1, -1]

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    if not head or not head.next or not head.next.next: # If there is only two nodes, then there are no critical points.
      return [-1, -1]
    
    p = head
    c = head.next
    critical_points = []
    i = 1
    
    while c.next: # Find critical points
      if (p.val < c.val > c.next.val) or (p.val > c.val < c.next.val): # Found maxima or minima
        critical_points.append(i)
        
      p = c
      c = c.next
      i += 1
    
    if len(critical_points) < 2: # Check if there are more 2 critical points to compare distances
      return [-1, -1]
    
    # Find min and max distances
    min_dist = float('inf')
    for i in range(1, len(critical_points)):
      min_dist = min(min_dist, critical_points[i] - critical_points[i-1])
    
    max_dist = critical_points[-1] - critical_points[0]
    return [min_dist, max_dist]
    

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Example usage
arr = [5, 3, 1, 2, 5, 1, 2]
head = create_linked_list(arr)
s = Solution()
print(s.nodesBetweenCriticalPoints(head))