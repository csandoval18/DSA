# O(n^3) time complexity
def maxProduct(nums):
  maxProd = 1
  
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      curr_product = 1
      for k in range(i, j+1):
        curr_product *= nums[k]
      
      maxProd = max(maxProd, curr_product)
  return maxProd
  
nums = [2,3,-2,4]
print(maxProduct(nums))