# Remove Nth Node From End of List
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  
# [1,2,3,4,5]
# n = 2
# 1 -> 2 -> 3 -> 4 -> 5
# ans:
# 1 -> 2 -> 3 -> 5
def removeNthFromEndAttempt(head, n):
  # 1. Traverse through list first to get length
  # 2. len(linkedlist) - n = index of node to remove
  node = head
  listLen = 0
  
  # Get linked list length
  while node:
    listLen += 1
    node = node.next
  if listLen - n < 0: return None
  if listLen == 1 and n == 1: return None
  # Reset node pointer to linked list head
  # Get index of node to remove at x, but we need to begin tracking at x-1 to set it as prev 
  # and then go to the next node, set the next pointer to the node.next and set the prev.next
  # the next pointer 
  node = head
  prev = ListNode()
  x = listLen - n
  i = 0
  
  while i <= x:
    if i == x-1:
      prev = node
    if i == x:
      nxt = node.next
      prev.next = nxt
      break
    node = node.next
    i += 1
  return head
  
  
def removeNthFromEnd(head, n):
  dummy = ListNode(0, head)
  left = dummy
  right = head
  
  # shift right to n spaces from left
  # L R R R
  # 0 1 2 3 4 5
  while n > 0 and right:
    right = right.next
    n -= 1
  
  while right:
    left = left.next
    right = right.next
  
  # Remove left's next node
  left.next = left.next.next
  return dummy.next
  
  
# ------------------------------------------------- 
    
# Print linked list as arr
def printLinkedListAsArr(node): 
  ll_arr = []
  while node:
    ll_arr.append(node.val)
    node = node.next
  print(ll_arr)
  
# Create test arr for ans 
head = ListNode(1)
node = head
for i in range(1,5): 
  node.next = ListNode(i+1)
  node = node.next

n = 2
printLinkedListAsArr(head)
ans = removeNthFromEnd(head, n)
print("ans:")
printLinkedListAsArr(ans)
