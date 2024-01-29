# 46. Permutations

def permute(nums: [int]) -> [[int]]:
  n = len(nums)
  
  def backtrack(idx: int):
    if idx == n:
      res.append(nums[:])
      return 
      
    for i in range(idx, n):
      nums[idx], nums[i] = nums[i], nums[idx]
      backtrack(idx+1)
      nums[idx], nums[i] = nums[i], nums[idx]  
    
  res = []
  backtrack(0)
  return res

nums = [1,2,3]
print(permute(nums))