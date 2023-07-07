def majorityElement( nums):
  hm = {}
  
  for i in nums:
    if i not in hm:
      hm[i] = 1
    else:
      hm[i] += 1
  
  maxNum = list(hm.values())
  maxKey = list(hm.keys())
  return maxKey[maxNum.index(max(maxNum))]
  # return max(hm, key=lambda x:hm[x])
  
print(majorityElement([3,3,4]))
