def findMaxConsecutiveOnes(nums):
  maxOnes = 0
  currSum = 0
  
  for n in nums:
    if n == 1:
      currSum += 1
      maxOnes = max(maxOnes, currSum)
    elif n != 1:
      currSum = 0
    
  return maxOnes
  