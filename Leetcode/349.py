class Solution(object):
  def intersection(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1.intersection(set2))

class Solution(object):
  def intersection(self, nums1, nums2):
    # Create dictionaries to count the occurances of elements in each array
    count1 = {}
    count2 = {}
    
    # Count occurences in nums1
    for n in nums1:
      count1[n] = count1.get(n, 0) + 1

    # Count occurences in nums2
    for n in nums2: 
      count2[n] = count2.get(n, 0) + 1
    
    # Find the common elements by checking the dictionaries
    common_elements = []
    for n in count1:
      if n in count2:
        common_elements.append(n)
        
    return common_elements
    
    