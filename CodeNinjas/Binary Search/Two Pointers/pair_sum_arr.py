def pairSum(arr, s):
  arr.sort()
  l, r = 0, len(arr)-1
  res = []
  
  while l<r:
    _sum = arr[l] + arr[r]
    
    if _sum == s:
      res.append(sorted((arr[l], arr[r])))
      r -= 1
    elif _sum < s:
      l += 1
    else:
      r -= 1
  return res
      
# arr = [1,2,3,4,5]
arr = [2,-6,2,5,2] 
s = 5
print(pairSum(arr, s))

def pair_sum(arr, s):
  n = len(arr)
  ans = []
  for i in range(n):
    for j in range(i+1, n):
      if arr[i] + arr[j] == s:
        temp = [min(arr[i], arr[j]), max(arr[i], arr[j])]
        ans.append(temp)
  ans.sort()
  return ans