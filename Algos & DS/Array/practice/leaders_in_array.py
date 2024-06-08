# A leader an element in the array that has no greater numbers to its right of its current index
# Ex: [10,22,12,3,0,6] output: [22,12,6] since they have no greater values to their right

# Brute Force:
def superiorElementsBF(a):
  n = len(a)
  res = []
  
  for i in range(n-1):
    curr = a[i]
    for j in range(i+1, n):
      if curr > a[j]:
        if j == n-1:
          res.append(curr)
        continue
      else:
        break
  res.append(a[n-1])
  
  return  res
  
a = [10,22,12,3,0,6] 
print(superiorElementsBF(a))
 
# Optimal 
# 1. Traverse from right to left of arr
# 2. Keep track of right elements's max to compare to curr elements

def superiorElementsOP(a):
  n = len(a)
  right_max = float('-inf')
  res = []
  
  for i in range(n-1, -1, -1):
    if a[i] > right_max:
      res.append(a[i])
      
    right_max = max(right_max, a[i])
  
  return res[::-1]
    

print(superiorElementsOP(a))
    