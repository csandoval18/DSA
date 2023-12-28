# def pairSum(arr, s):
#   arr.sort()
#   l, r = 0, len(arr)-1
#   res = []
  
#   while l<r:
#     curr_sum = arr[l] + arr[r]
    
#     if curr_sum == s:
#       res.append(sorted((arr[l], arr[r])))
#       r -= 1
#       l += 1
#     elif curr_sum < s:
#       l += 1
#     else:
#       r -= 1
#   return res

def pairSum(arr, s):
  # Write your code here.
  arr.sort()
  l, r = 0, len(arr)-1
  res = []
  
  while l<r:
    curr_sum = arr[l] + arr[r]
    
    if curr_sum == s:
      tmp = [min(arr[l], arr[r]), max(arr[l], arr[r])]
      res.append(tmp)
      r -= 1
    elif curr_sum < s:
      l += 1
    else:
      r -= 1
  res.sort()
  return res

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
  
  
# arr = [1,2,3,4,5]
# arr = [2,-6,2,5,2] 
arr = [2,-3,3,3,-2]
s = 0
print(pairSum(arr, s))