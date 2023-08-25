def maxSubArray(self, nums):
  # Start max_sum as float('-inf') to take negative numbers into account
  max_sum = float('-inf')
  current_sum = 0
  
  for n in nums:
    current_sum = max(n, current_sum + n)
    max_sum = max(max_sum, current_sum)
  
  return max_sum
  
nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5,4,-1,7,8]


# Iteration 0 
# n = -2
# current_sum = max(-2, 0 + -2) = -2
# max_sum = max(float('-inf'), -2) = -2

# Iteration 1
# n = 1  

