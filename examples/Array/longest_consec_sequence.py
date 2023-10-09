# Longest Consecutive Sequence #128 LC
def longestSequence(nums):
  n = len(nums)
  if n == 0:
    return 0
  
  maxCount = 0
  count = 1
  hs = set()
  for num in nums:
    hs.add(num)
  
  for num in hs:
    if num-1 not in hs:
      i = 0
      x = num
      while x+1 in hs:
        count += 1
        x += 1
      maxCount = max(maxCount, count) 
  return maxCount

nums = [102,4,100,1,101,3,2]
    