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
      for k in range(i, j):
        currSum += nums[k]

      if currSum == k:
        count += 1
       
  return count
  
def subarraySumBetter(nums, k):
# nums = [1,1,1]
# k = 2
# How many subarrays add up to k?
# Output: 2

nums = [1,2,3]
print(subarraySum(nums, 2))