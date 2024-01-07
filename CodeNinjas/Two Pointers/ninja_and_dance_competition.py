def kDiffPairs(arr, n, k):
  hm = {}
  pairs = set()
  
  for num in arr:
    hm[num] = hm.get(num, 0)+1
  
  for num in arr:
    diff = k+num
    if diff in hm:
      pairs.add((diff,num))
      hm[diff] -= 1
      if hm[diff] == 0:
        hm.pop(diff)
    
  return len(pairs)
  
  

# k = x - 2
# 3 = x - 2
# 3+2 = x
# 5 = x

# arr = [2,6,5,2,3]
# k = 3
arr = [1,1,2,2]
k = 1
print(kDiffPairs(arr, len(arr), k))