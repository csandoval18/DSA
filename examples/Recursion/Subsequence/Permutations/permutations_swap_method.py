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
print()

def permute1(nums: [int]) -> [[int]]:
  n = len(nums)
  res = []
  
  def backtrack(idx: int):
    if idx == n-1:
      res.append(nums[:])
      return
    
    for i in range(idx, n):
      nums[i], nums[idx] = nums[idx], nums[i]
      backtrack(idx+1)
      nums[i], nums[idx] = nums[idx], nums[i]
    
  backtrack(0)
  return res

arr1 = [1,2,3]
print(permute1(arr1))
print()


# Either n or n-1 work to start backtracking n-1 just ends it quicker and doesn't take the case where idx == n and is out
# of range of an element 
def permute2(nums: [int]) -> [[int]]:
  n = len(nums)
  res = []
  
  def backtrack(idx: int) -> None:
    if idx == n-1:
      res.append(nums[:])
      return
      
    for i in range(idx, n):
      nums[i], nums[idx] = nums[idx], nums[i]
      backtrack(idx+1)
      nums[i], nums[idx] = nums[idx], nums[i]
  
  backtrack(0)
  return res

arr = [1,2,3]
print(permute2(arr))