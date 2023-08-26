#  Brute force approach (not accepted by lc)
def productExceptSelfBruteForce(nums):
  answer = []
  
  for i in range(len(nums)):
    tmp = nums[:i] + nums[i+1:]
    # non mutable
    # tmp = [n for i, n in enumerate(nums) if ]]
    product = 1
    for n in tmp:
      product *= n
    answer.append(product)
    
  return answer






# O(n) and O(n) space
def productExceptSelfExtraSpace(nums):
  n = len(nums)
  
  prefix = [1] * n
  suffix = [1] * n
  output = []
  
  # Calculate prefix products
  prefix_product = 1
  for i in range(n):
    prefix[i] = prefix_product
    prefix_product *= nums[i]
  
  # Calculate suffix products
  suffix_product = 1
  for i in range(n-1, -1, -1):
    suffix[i] = suffix_product
    suffix_product *= nums[i]
    
  # Calculate output array
  for i in range(n):
    output[i] = prefix[i] * suffix[i]
  
  return output
  
  
  
  
  
# O(n) and O(1) space
def productExceptSelf(nums):
  res = [1] * len(nums)
  
  prefix = 1
  for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i] 
    
  suffix = 1
  for i in range(len(nums) -1, -1, -1):
    res[i] *= suffix
    suffix *= nums[i]
    
  return res
    
nums = [1,2,3,4]
print(productExceptSelf(nums))

# Added a 1 at start since index 0 would check left of prefix which is out of range of array
# Prefix of [1,2,3,4] = [1] + [1,2,6,24]
# Suffix of [1,2,3,4] = [24,24,12,4] + [1]