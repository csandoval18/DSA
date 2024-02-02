class Solution(object):
    def containsDuplicate(self, nums):
      hm = {}
      
      for i, n in enumerate(nums):
        if n not in hm:
          hm[n] = 1
        else:
          hm[n] += 1

      return True if max(list(hm.values())) >= 2 else False



#fastest
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)