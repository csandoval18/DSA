from typing import List

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