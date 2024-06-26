# O(n^3)
def max_subarray(nums):
  n = len(nums)
  for i in range(n):
    for j in range(i, n):
      curr_sum = 0
      
      # Subarray that k traverses => subarray = nums[i:j+1]
      for k in range(i, j+1):
        curr_sum += nums[k]
      
      max_sum = max(max_sum, curr_sum)
      
  return max_sum
        
      

  
# Neetcode Kadane Solution
def maxSubArrayNeetCode(nums):
  max_sum = float('-inf')
  curr_sum = 0
  
  for n in nums:
    # Ignore negative numbers
    if n < 0:
      curr_sum = 0
    curr_sum += n
    max_sum = max(max_sum, curr_sum)
  return max_sum
  
  

# Kadane's algorithm O(n) complexity
def maxSubArray(nums):
  # Start max_sum as float('-inf') to take negative numbers into account
  max_sum = float('-inf')
  current_sum = 0
  
  for n in nums:
    current_sum = max(n, current_sum + n)
    max_sum = max(max_sum, current_sum)
  
  return max_sum
  
  
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5,4,-1,7,8]
nums = [1,2,3,4]
print(max_subarray(nums)) 



# Iteration 0 
# n = -2
# current_sum = max(-2, 0 + (-2) = -2) = -2
# max_sum = max(float('-inf'), -2) = -2 -----

# Iteration 1
# n = 1  
# current_sum = max(1, -2 + 1= -1 ) = 1
# max_sum = max(-2, 1) = 1 -----

# Iteration 2
# n = -3
# current_sum = max(-3, 1 + (-3) = -2) = -2
# max_sum = max(1, -2) = 1 -----

# Iteration 3
# n = 4
# current_sum = max(4, -2 + 4 = 2) = 4
# max_sum = max(1, 4) = 4 -----

# Iteration 4
# n = -1
# current_sum = max(-1, 4 + (-1) = 3) = 3
# max_sum = max(4, 3) = 4 -----

# Iteration 5
# n = 2 
# current_sum = max(2, 3 + 2 = 5) = 5
# max_sum = max(4, 5) = 5 -----

# Iteration 6
# n = 1 
# current_sum = max(1, 1 + 5 = 6) = 6
# max_sum = max(5, 6) = 6 -----

# Iteration 7
# n = -5
# current_sum = max(-5, 6 + -5) = 1
# max_sum = max(6, 1) = 6 -----

# Iteration 8
# n = 4
# current_sum = max(4, 1 + 4 = 5) = 5
# max_sum = max(6, 5) = 6 -----


# //////////////////////////////////////////////////////////////////////////////////////////////

# nums = [5,4,-1,7,8]

# max_sum = float('-inf')
# current_sum = 0

# for n in nums:
#   curr_sum = max(n, curr_sum + n)
#   max_sum = max(max_sum, curr_sum)

# Iteration 0 
# n = 5
# current_sum = max(5, 0 + 5) = 5
# max_sum = max(float('-inf'), 5) = 5

# Iteration 1
# n = 4  
# current_sum = max(4, 5 + 4 = 9) = 9
# max_sum = max(5, 9) = 9

# Iteration 2
# n = -1
# current_sum = max(-1, 9 + (-1) = 8) = 8
# max_sum = max(9, 8) = 9

# Iteration 3
# n = 7
# current_sum = max(7, 8 + 7 = 15) = 15
# max_sum = max(9, 15) = 15

# Iteration 4
# n = 8
# current_sum = max(8, 15 + 8 = 23) = 23
# max_sum = max(16, 23) = 23
