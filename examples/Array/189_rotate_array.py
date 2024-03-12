from typing import List


# Array is modified in place

def rotate(nums: List[int], k: int) -> List[int]:
  n = len(nums)
  k = k%n
  nums[:] = nums[-k:] + nums[:-k]


def rotate2(nums: List[int], k: int) -> List[int]:
  n = len(nums)
  k = k%n
  
  nums.reverse()
  nums[:k] = reversed(nums[:k])
  nums[k:] = reversed(nums[k:])
  
# We use k % n to handle cases where the number of steps k is greater than the length of the array n.

# Consider the following scenario: if you have an array of length n and you rotate it by k steps, where 
# k is greater than n, the effect of rotating k steps is equivalent to rotating the array by k % n steps.

# For example, if you have an array of length 5 and you rotate it by 7 steps, you effectively rotate it 
# by 7 % 5 = 2 steps. This is because after rotating by 5 steps, you would end up with the same array, so 
# rotating by any multiple of 5 has no effect on the final array. Therefore, we take the modulus (%) of k 
# with n to handle cases where k is greater than n, effectively reducing it to the equivalent number of 
# steps needed within the range of the array's length.