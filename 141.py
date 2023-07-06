class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Floyd's Tortoise & Hare Algorithm (slow and fast pointers)

# FT&H algorithm works on the proof that the slow and fast pointers will 
# equal each other0
def hasCycle(head):
  # start at same location
  slow, fast = head, head
  
  # while faster node does not reach a null
  while fast and fast.next:
    # slow pointer moves 1 node forward
    slow = slow.next   
    # fast pointer moves 2 nodes forward
    fast = fast.next.next
    
    if slow == fast:
      return True
  return False
    
