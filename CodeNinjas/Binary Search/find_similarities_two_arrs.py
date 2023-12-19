# Find similarities between two arrays
# 1. Return num of elements common to arr1 and arr2
# 2. Return number of els in the union of arr1 and arr 2 
# (num of unique numbers in the merge of arr1 and arr2)

# [1,2,3,4,5]
# [4,6,2]

# BF
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



    
    
      
  
  
  
  
  
  
      
      
      
    
    
    
  