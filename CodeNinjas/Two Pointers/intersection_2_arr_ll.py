from typing import List


class SolutionHM:
  def intections(self, arr1: List[int], n: int, arr2: List[int], m: int):
    st = set()
    res = []
    
    for num in arr2:
      if num not in st:
        st.add(num)
    
    for num in arr1:
      if num in st:
        res.append(num)
        st.remove(num)
    
    return res
  
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1.sort()
        nums2.sort()
        i = 0
        for num in nums1:
            if i >= len(nums2):
                break
            while i < len(nums2) - 1 and nums2[i] < num:
                i += 1
            if nums2[i] == num:
                i += 1
                intersection.append(num)

        return intersection