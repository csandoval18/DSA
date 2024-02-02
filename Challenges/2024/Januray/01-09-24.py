from collections import defaultdict, deque
from typing import Optional

# 2385. Amount of Time for Binary Tree to Be Infected

class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

# 1. Find infected node val
# 2. Perform BFS since it searches for all adjacent nodes first compared to reaching a max depth
# first such as in dfs

def amountOfTime(root: Optional[TreeNode], start: int) -> int:
  def findNode(root: Optional[TreeNode], start):
    if not root:
      return 0
    
    # Each element in the queue is a tuple
    queue = deque([(root, 0)]) 
    max_time = 0
    
    while queue:
      curr_node, time = queue.popleft()
      
      # Update the max time
      max_time = max(max_time, time)
      
      # Add uinfected adjacent nodes to the queue
      if curr_node.left and curr_node.left.val != start:
        queue.append((curr_node.left, time+1))
      if curr_node.right and curr_node.right.val != start:
        queue.append((curr_node.right, time+1))
      
    return max_time
    
    
def amountOfTimeSolution(root: Optional[TreeNode], start: int) -> int:
  graph=defaultdict(list)
  stack=[(root,None)]
  
  while stack:
    n,p=stack.pop()
    if p:
      graph[p.val].append(n.val)
      graph[n.val].append(p.val)
    if n.left:
      stack.append((n.left,n))
    if n.right:
      stack.append((n.right,n))
      
  ans=-1
  seen={start}
  queue=deque([start])
  
  while queue:
    for _ in range(len(queue)):
      u=queue.popleft()
      for v in graph[u]:
        if v not in seen:
          seen.add(v)
          queue.append(v)
    ans+=1
  return ans 
  
def amountOfTime(root: Optional[TreeNode], start: int) -> int:
  def findInfectedNode(root, start):
    if not root:
      return
    
    if root.val == start:
      return root
    
    # Check left subtree
    left_res = findInfectedNode(root.left, start)
    if left_res:
      return left_res
    
    # Check right subtree
    right_res = findInfectedNode(root.right, start)
    return findInfectedNode(root.right, start)
  
  return findInfectedNode(root, start)


# Creating tree
n9 = TreeNode(9)
n2 = TreeNode(2)

n4 = TreeNode(4, n9, n2)
n10 = TreeNode(10)
n6 = TreeNode(6)

n3 = TreeNode(3, n10, n6)
n5 = TreeNode(5, None, n4)

n1 = TreeNode(1, n5, n3)

resNode = amountOfTime(n1, 3)
print(resNode.val)
print(resNode.left.val)
print(resNode.right.val)
