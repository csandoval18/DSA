# Find similarities between two arrays
# 1. Return num of elements common to arr1 and arr2
# 2. Return number of els in the union of arr1 and arr 2 
# (num of unique numbers in the merge of arr1 and arr2)

# [1,2,3,4,5]
# [4,6,2]

# Using sets (hm can set turned into set)
# O(n+m)
def findSimilarity(arr1, arr2, n, m):
  hm = {} 
  commonEls = 0
  uniqueNums = set()
  
  for num in arr1:
    hm[num] = hm.get(num, 0)+1
    # Get num of unique elements in arr1
    if num not in uniqueNums:
      uniqueNums.add(num)
    
  
  # Get common elements found in both arrs
  for num in arr2:
    if num in hm:
      commonEls += 1
    if num not in uniqueNums:
      uniqueNums.add(num)
  
  return commonEls, len(uniqueNums)

# BS
# O(N log N)

def binarySearch(arr, t):
  l, r = 0,1
  
  while l<=r:
    m = (l+r)//2
    
    if arr[m] == t:
      return True
    elif arr[m] < t:
      l = m+1
    else:
      r = m-1
  return False

def findSimilaritBS(arr1, arr2):
  arr1.sort()
  arr2.sort()
  
  common_els = []
  unique_els = []
  
  for num in arr1:
    if binarySearch(arr2, num): 
      common_els.append(num)
    else:
      unique_els.append(num)
  
  for num in arr2:
    if not binarySearch(arr1, num):
      unique_els.apend(num)
      
  return common_els, unique_els
  
  