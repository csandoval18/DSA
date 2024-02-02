class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
    hm = {}
    
    for i, n  in enumerate(nums):
      # To get duplicate you can just check if the number is already in the hm
      if n in hm and abs(hm[n] - i) <= k:
        return True
      hm[n] = i
    return False

nums = [1, 2, 3, 1]
k = 3

ans = Solution()
print(ans.containsNearbyDuplicate(nums, k))