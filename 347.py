# 347. Top K Frequent Elements  

# k = 2
# [1,1,1,2,2,3], 

# Output: [1,2]
def topKFrequent(nums, k):
  n = len(nums)
  res = []
  cnt = 0
  
  for i in range(n):
    cnt += 1
    
    