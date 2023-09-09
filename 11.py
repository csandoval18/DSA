# O(n) 2 pointer solution
def maxArea(height):
  n = len(height)
  max_area = float('-inf')
  l = 0
  r = n-1
  
  while l < r:
    # Calculate area & update max area
    dist = r - l
    min_height = min(height[l], height[r])
    max_area = max(max_area, dist * min_height)
    
    # Reduce smaller pointer val
    if height[l] < height[r]:
      l += 1
    else:
      r -= 1
  
  return max_area

height = [4,1,6,3,5,2]
print(maxArea(height))
  