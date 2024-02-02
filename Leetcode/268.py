class Solution(object):
  def missingNumber(self, nums):
    nums.sort()
    i = 0
    
    for n in nums:
      if i != n:
        return i
      i += 1
    return i
    
nums = [3, 0, 1]
sol = Solution()
print(sol.missingNumber(nums))

