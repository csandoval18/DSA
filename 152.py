# O(n^3) time complexity
def maxProduct(nums):
  maxProd = float('-inf')
  
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      curr_product = 1
      for k in range(i, j+1):
        curr_product *= nums[k]
      
      maxProd = max(maxProd, curr_product)
  return maxProd

# O(n^2) time complexity
def maxProductBruteForce(nums):
  max_prod = float('-inf')
  
  for i in range(n):
    curr_prod = 1
    for j in range(i, len(nums)):
      curr_prod *= nums[j]
      max_prod = max(max_prod, curr_prod)
      
  return max_prod
  
# Chatgpt O(n)
def max_product_subarray(nums):
  # Base case
  if len(nums) == 0:
    return 0
  
  max_prod = nums[0]
  min_prod = nums[0]
  
  for i in range(1, len(nums)):
    if nums[i] < 0:
      max_prod, min_prod = min_prod, max_prod
  
    max_prod = max(nums[i], max_prod * nums[i])
    min_prod = min(nums[i], min_prod * nums[i])
    
    result = max(result, max_prod)
  
  return result
  
  
# Neetcode
def maxProdNeetcode(nums):
  res = max(nums)
  currMin, currMax = 1, 1
  
  for n in nums:
    if n == 0:
      currMin, currMax = 1, 1
      continue
    
    tmp = currMax * n
    currMax = max(n * currMax, n * currMin, n) 
    currMin = min(tmp, n * currMin, n) 
    res = max(res, currMax)
    
  return res
  
  
# Observation approach

# 1. All positive elements, then multiply all numbers and return product
# 2. Even count of negative elements, multiply all and return product
# 3. Odd negatives, get prefix max and suffix max similar to the the problem product of array except self 
# 4. If the array contains 0s, then product = 0, therefore they should be ignored
  
def maxProdSubarray(nums):
  prefix, suffix = 1, 1
  res = float('-inf')
  
  for i in range(len(nums)):
    if prefix == 0: pre = 1
    if suffix == 0: suff = 1
    
    prefix *= nums[i]
    suffix *= nums[len(nums)-1-i]
    res = max(res, prefix, suffix)
  return res
  
nums = [2,3,-2,4]
