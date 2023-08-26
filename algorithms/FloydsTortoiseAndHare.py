# The "tortoise and hare" algorithm, also known as Floyd's 
# cycle detection algorithm or the "cycle detection algorithm," is a 
# technique used to detect cycles in linked lists or sequences. 
# This algorithm is often used in various contexts, such as finding a cycle in a 
# linked list or determining if there's a repeating pattern in a sequence.

# Steps:

# 1. Start with two pointers: the "tortoise" (slow pointer) and the "hare" (fast pointer). 
# Both initially point to the first element in the linked list or sequence.

# 2. Move the tortoise one step at a time and the hare two steps at a time.

# 3. If there is a cycle in the linked list or sequence, the hare will eventually 
# catch up to the tortoise as they move through the cycle.

# 4. If there is no cycle, the hare will reach the end of the linked list or sequence, and the algorithm terminates.

class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None
  
def has_cycle(head):
  tortoise = hare = head
  
  while hare is not None and hare.next is not None:
    # tortoise advances by 1 step
    tortoise = tortoise.next
    #  hare advances by 2 steps
    hare = hare.next.next
    
    if tortoise == hare:
      return True # Cycle detected
    
  return False # No cycle detected
  
  
  
    