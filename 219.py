class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
    hm = {}
    
    for i, n  in enumerate(nums):
      hm[n] = i
    
    return hm

nums = [1, 2, 3, 1]
k = 3

ans = Solution()
print(ans.containsNearbyDuplicate(nums, k))