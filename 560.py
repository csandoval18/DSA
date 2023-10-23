# def subarraySum(nums, k):
#   n = len(nums)
#   res = 0
  
#   for i in range(n):
#     for j in range(i, n):
#       subarr = []
#       for l in range(i, j+1):
#         res += nums[l]
#         subarr.append(nums[l])
#       print(subarr)
#   return res

def subarraySumBF(nums, k):
  n = len(nums)
  count = 0
  
  for i in range(n):
    for j in range(i,n):
      currSum = 0
      for k in range(i, j+1):
        currSum += nums[k]

      if currSum == k:
        count += 1
       
  return count
  
def subarraySumBetter(nums, k):
  n = len(nums)
  count = 0
  
  for i in range(n):
    curr_sum = 0
    for j in range(i, n):
      curr_sum += nums[j]
    
    if curr_sum == k:
      count += 1
    
  return count
  
def subarraySumOP(nums, k):
  hm = {0:1}
  curr_sum = 0
  count = 0

  for i in range(len(nums)): 
    curr_sum += nums[i]
    if curr_sum - k in hm:
      count += hm[curr_sum-k]
    hm[curr_sum] = hm.get(curr_sum, 0) + 1
  
  return count
  
# nums = [1,1,1]
# k = 2
# How many subarrays add up to k?
# Output: 2

nums = [1,2,3]
print(subarraySum(nums, 2))