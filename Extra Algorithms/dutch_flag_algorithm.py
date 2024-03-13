# Optimal Solution:
# O(n) 
# 0   low-1 low   mid-1 mid             high high+1    n-1
# |       | |         | |                  | |           |
# 0 0 0 0 0 1 1 1 1 1 1 0s/1s/2s (unordered) 2 2 2 2 2 2 2


def sort_colors(nums: [int]) -> [int]: 
  low = 0
  mid = 0
  high = len(nums)-1
  
  while mid <= high:
    if nums[mid] == 0:
      # swap(mid, low)
      nums[low], nums[mid] = nums[mid], nums[low]
      low += 1
      mid += 1
    
    elif nums[mid] == 1:
      mid += 1
    
    elif nums[mid] == 2:
      # swap(mid, high)
      nums[mid], nums[high] = nums[high], nums[mid]
      high -= 1
      
  return nums