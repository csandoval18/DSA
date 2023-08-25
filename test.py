# for i in range(2, 0):
#   print("hello")

# arr = [1,2,3,4,5]
# print("arr len:", len(arr))


def maxProfit(prices):
  l = 0
  maxP = 0

  for r in range(1, len(prices)):
    # Check if price of previous day in pointer "l" is smaller than pointer "r"
    # If it is smaller this indicates that there is a profit since you could buy
    # stock at a cheaper prices the previous day "l" and sell the current day "r"
    if prices[l] < prices[r]: 
      # Calculate profit made 
      profit = prices[r] - prices[l]
      # Update new max profit
      maxP = max(maxP, profit)
    # This part below is necessary
    # It updates the left pointer to be the right since the price in pointer "l" is greater than 
    # in pointer "r". This means that there is no profit to be made therefore "l" need to be updated to the 
    # lower price which is pointer "r" in that iteration
    else:
      l = r
  return maxP

prices = [7,1,5,3,6,4]
print(maxProfit(prices))





def productExceptSelf(nums):
  n = len(nums)
  prefix = [1] * n
  suffix = [1] * n
  res = [0] * n

  print("Initial prefix array:", prefix)

  prefix_product = 1
  for i in range(n):
    prefix_product *= nums[i]
    prefix[i] = prefix_product
    print(f"Step {i + 1} - Prefix Array:", prefix)

  prefix = [1] + prefix
  print("Final Prefix Array:", prefix)
  print("\n")
  print("Initial prefix array:", suffix)
  
  # Calculate right suffix products
  right_product = 1
  for i in range(n - 1, -1, -1):
    right_product *= nums[i]
    suffix[i] = right_product
    print(f"Step {i + 1} - Suffix Array:", suffix)
  
  suffix = suffix + [1]
  print("Final Suffix Array:", suffix)
  print("\n")
  print("Initial res array:", res)
  
  # Calculate output array
  for i in range(n):
    res[i] = prefix[i] * suffix[i+1]
    print(f"Step {i} - Result Array:", res)
  print("Final Result Array:", res)
  return res
    

nums = [1,2,3,4]
productExceptSelf(nums)

# Prefix of [1,2,3,4] = [1,1,2,6]
# Suffix of [1,2,3,4] = [24,24,12,4]



def productExceptSelfWithActualPrefixAndSuffixArrays(nums):
  n = len(nums)
  prefix = [1] * n
  suffix = [1] * n
  res = [0] * n

  prefix_product = 1
  for i in range(n):
    prefix_product *= nums[i]
    prefix[i] = prefix_product
    
  prefix = [1] + prefix
  
  # Calculate right suffix products
  right_product = 1
  for i in range(n - 1, -1, -1):
    right_product *= nums[i]
    suffix[i] = right_product
  
  suffix = suffix + [1]
  
  # Calculate output array
  for i in range(1,n):
    res[i] = prefix[i-1] * suffix[i+1]
    
  return res