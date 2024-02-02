def longestConsecutiveBruteForce(nums):
  n = len(nums)
  if n == 0:
    return 0
  
  longest = 1
  hs = set()
  
  # Put all array elements into set
  for i in range(n):
    hs.add(nums[i])
    
  # Find longest sequence
  for num in hs:
    # if it is a starting num
    if num-1 not in hs:
      # find consecutive nums
      cnt = 1
      j = num
      while j+1 in hs:
        j += 1
        cnt += 1
      longest = max(longest, cnt)
  return longest
  
nums = [100,4,200,1,3,2]