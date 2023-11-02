# a = [1,2,3,4,5,6,2,8]
# hm to keep count 
# return [P,Q]
# P = el that appears once
# Q = missing num in range(1, n)

#Brute Force O(n^2) 
def findMissingRepeatingNumbers(a: [int]) -> [int]:
  n = len(a)
  tracker = 1
  hm = {}
  res = [0,0]
  
  for i in range(n):
    # Find repeating number w/ hm
    if a[i] in hm:
      res[0] = a[i]
    else:
      hm[a[i]] = hm.get(a[i], 0) + 1
      
  # Find missing num
  for num in a:
    if tracker not in hm:
      res[1] = tracker
    tracker += 1
  return res

a = [1,2,3,2]
print(findMissingRepeatingNumbers(a))
    
# Optimal Math O(n)

  