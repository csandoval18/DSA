def checkFirstAttempt(nums):
  minVal = nums[0]
  for i in range(1, len(nums)):
    if nums[i-1] > nums[i]:
      for j in range(i, len(nums)):
        if nums[j] > minVal:
          return False
      return True
  return True
  
# nums = [3,4,5,1,2]
# nums = [2,1,3,4]
# nums = [1,2,3,4,5]
# First attempt breaks with array below 
nums = [8,5,4,5,1,4,5,2,2]

print(check(nums))