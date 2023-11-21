def searchRangeA(nums: [int], target: int) -> [int]:
  n = len(nums)
  l = 0
  r = n-1
  
  while l<=r:
    m = (l+r)//2
    
    if nums[m] == target:
      a = m
      b = m
      while nums[a] == nums[m]:
        a -= 1
      while nums[b] == nums[m]:
        b += 1
      return [a+1,b-1]
    elif nums[m] >= target:
      r = m-1
    else:
      l = l+1
  return [-1, -1]


def find_start(nums: [int], target: int) -> [int]:
  n = len(nums)
  l = 0
  r = n-1
  start = -1
  
  while l<=r:
    m = (l+r)//2
    
    if nums[m] == target:
      start = m
      l = m+1
    elif nums[m] > target:
      r = m-1
    else:
      l = m+1
  return start 

def find_end(nums: [int], target: int) -> [int]:
  n = len(nums)
  l, r = 0, n-1
  end = -1
  
  while l<=r:
    m = (l+r)//2
    
    if nums[m] == target:
      end = m
      l = m+1
    elif nums[m] > target:
      r = m-1
    else:
      l = m+1
  return end
  
nums = [5,7,7,8,8,10]
target = 8
print(find_start(nums, target))