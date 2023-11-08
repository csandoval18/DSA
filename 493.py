from types import List

def reversePairs(nums: [int]) -> int:
  def mergeSort(nums, l, r):
    if l >= r:
      return count
    
    m = (l+r) // 2
    count = mergeSort(nums, l, m) + mergeSort(nums, m+1, r)
    
    j = m+1
    for i in range(l, m+1):
      while j <= r and nums[i] > 2 * nums[j]:
        j += 1
      count += j - (m+1)
      
    nums[l:r+1]  = sorted(nums[l:r + 1])
    return count
    
  return mergeSort(nums, 0, len(nums) - 1)
    
  
nums = [1,3,2,3,1]
reversePairs(nums)

def reversePairs(nums):
  tmp = []
  
  