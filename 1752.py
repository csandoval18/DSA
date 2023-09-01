def checkFirstAttempt(nums):
  minVal = nums[0]
  for i in range(1, len(nums)):
    if nums[i-1] > nums[i]:
      for j in range(i, len(nums)):
        if nums[j] > minVal:
          return False
      return True
  return True
  
# First attempt breaks with array below 
# nums = [8,5,4,5,1,4,5,2,2]


# Modulo "wrap around" solution
# next = (i+1) % n

def checkModulo(nums):
  n = len(nums)
  increasing_count = 0
  
  for i in range(n):
    if nums[i] > nums[(i+1) % n]:
      increasing_count += 1
      if increasing_count > 1:
        return False
  return True if increasing_count == 0 or nums[0] >= nums[n-1] else False

# Not using modulo
def check(nums):
  n = len(nums)
  increasing_count = 0
  
  for i in range(n):
    # Wrap around if index exceeds n-1
    if i+1 < n:
      next_index = i+1
    else: 
      next_index = 0
    
    if nums[i] > nums[next_index]:
      increasing_count += 1
      if increasing_count > 1:
        return False
  
  if increasing_count == 0 or nums[0] >= nums[n-1]:
    return True
  else:
    return False

# nums = [3,4,5,1,2]

# 3 

# nums = [2,1,3,4]
# nums = [1,2,3,4,5]
# nums = [8,5,4,5,1,4,5,2,2]

# print(check(nums))