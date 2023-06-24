def maxDepthIterative(self, root):
  if not root:
    return 0
  
  queue = [(root, 1)]
  max_depth = 0
  
  while queue:
    node, depth = queue.pop()
    max_depth = max(max_depth, depth)
    
    if node.left:
      queue.append((node.left, depth + 1))
    if node.right:
      queue.append((node.right, depth + 1))
  
  return max_depth
  
def maxDepth(self, root):
  if not root:
    return 0
  return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
  