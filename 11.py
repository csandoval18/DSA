# O
def maxArea(height):
  n = len(height)
  l = 0
  r = n-1
  maxArea = float('-inf')
  
  while l < r:
    width = r-l
    min_height = min(height[l], height[r])
    