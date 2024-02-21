from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
  n = len(nums)
  res = []
  
  def backtrack(freq: List[int], ds: List[int]):
    if len(ds) == n:
      res.append(ds[:])
      return
      
    for i in range(n):
      # Need to add this condition to not backtrack into duplicates in arr
      # i > 0 to not check the first index and checks if the curr num is the
      # same val as the last value and not in the freq or seen array
      # if  these conditions are met we have already added the permutations of
      # that starting value and do not need to repeat it
      if freq[i] or (i > 0 and nums[i] == nums[i-1] and not freq[i-1]):
        continue
        
      ds.append(nums[i])
      freq[i] = 1
      backtrack(freq, ds)
      freq[i] = 0
      ds.pop()
    
  freq = [0] * n
  nums.sort()
  backtrack(freq, [])
  return res

nums = [1,1,2]
print(permuteUnique(nums))

