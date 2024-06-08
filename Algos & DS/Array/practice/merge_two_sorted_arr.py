# Shortcut using a set and turning returned response to list
# hash sets only allow unique entries
# (Not accepted in codingninjas
def mergeSortedListUnique(a,b): 
  res = set()
  
  for num in a:
    res.add(num)
  
  for num in b:
    res.add(num)
  
  return list(res)

a = [1,2,3,3]
b = [2,2,4,5,5,5]
# print(sortedArray(a,b))
print(mergeSortedListUnique(a,b))


# The merged array can not contain duplicates

# Used hm to keep track of numbers already added to res
# Note to self: when adding hm checks, usually interrupting the iteration indexes
# can cause errors. Make sure if the check should be along the if statement or 
# inside the current if cluase

def sortedArray(a, b):
  n = len(a)
  m = len(b)
  i,j = 0,0
  hm = {}
  res = []
  
  while i < n and j < m:
    if a[i] < b[j]:
      if a[i] not in hm:
        res.append(a[i])
        hm[a[i]] = True
        i += 1
      else:
        i += 1
    elif a[i] > b[j]:
      if b[j] not in hm:
        res.append(b[j])
        hm[b[j]] = True
        j += 1
      else: 
        j += 1
    elif a[i] == b[j]:
      if a[i] not in hm:
        res.append(a[i])
        hm[a[i]] = True
        i += 1
        j += 1
      else:
        i += 1
        j += 1
  
  while i < n:
    if a[i] not in hm:
      res.append(a[i])
      hm[a[i]] = True
      i += 1
    else:
      i += 1
  
  while j < m:
    if b[j] not in hm:
      res.append(b[j])
      hm[b[j]] = True
      j += 1
    else:
      j += 1
      
  return res
  
  