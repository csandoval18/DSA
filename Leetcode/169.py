def majorityElement(nums):
  hm = {}
  
  for i in nums:
    if i not in hm:
      hm[i] = 1
    else:
      hm[i] += 1
  
  hmValues = list(hm.values())
  hmKeys = list(hm.keys())
  maxNum = max(hmValues)
  
  return hmKeys[hmValues.index(maxNum)]
  # return max(hm, key=lambda x:hm[x])
  
print(majorityElement([3,3,4]))

def majorityElement(nums):
    nums.sort()

    m = len(nums)//2
    l = m-1
    r = m+1
    if nums[l] == nums[m]:
        return nums[l]
    
    elif nums[m] == nums[r]:
        return nums[r]