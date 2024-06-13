from typing import List

# Approach
# The idea is to use the prefix sum technique and modular arithmetic to solve this problem efficiently.
# Here's the step-by-step explanation:

# 1. Prefix Sum and Modulo Operation:
  # Compute the prefix sum of the array up to each index.
  # Calculate the remainder of the prefix sum when divided by K (i.e., prefix_sum % K).
  # If two prefix sums have the same remainder when divided by K, the subarray between these two indices has a sum that is divisible by K.

# 2. Using a Hash Map:
  # Use a hash map to store the frequency of each remainder.
  # Initialize the hash map with the remainder 0 having a count of 1 (this handles the case where a subarray itself is directly divisible by K from the start).
  # As you iterate through the array, compute the prefix sum and its remainder.
  # If this remainder has been seen before in the hash map, it means there are subarrays ending at the current index which are divisible by K. Add the count of this remainder in the hash map to the result.
  # Update the hash map with the current remainder.

# 3. Handling Negative Remainders:
  # Ensure that remainders are always positive. If a remainder is negative, adjust it by adding K to get a positive equivalent.


class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    rem_cnt = {0: 1} # Initialized with {0: 1} to handle cases where the subarray sum itself is divisible by K from the start.
    curr_sum = 0
    count = 0
    
    for num in nums:
      curr_sum += num
      # Calculate the remainder
      rem = curr_sum % k
      
      # If this remainder has been seen before, it means there are subarrays
      # ending at the current index which are divisible by K.
      if rem < 0:
        rem += k
      
      # Update the hash map with the current remainder
      if rem in rem_cnt:
        count += rem_cnt[rem]
        rem_cnt[rem] += 1
      else:
        rem_cnt[rem] = 1
        
    return count


# Iterating Through the Array:
  # For each element in nums, update the prefix_sum.
  # Calculate the remainder of the prefix_sum when divided by K.
  # Adjust the remainder to be positive if it's negative.
  # If this remainder has been seen before, add the count of this remainder in remainder_count to result.
  # Update remainder_count with the current remainder, incrementing its count if it already exists or setting it to 1 if it doesn't.