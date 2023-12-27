# Code ninjas did not accept but it works

def findArraySum(a: [int], n: int, b: [int], m: int):
  p1, p2 = n-1, m-1
  res = []
  rem = 0
  
  while p1 >= 0 or p2 >= 0:
    curr_sum = a[p1]+b[p2]+rem
    
    res.insert(0, curr_sum%10)
    rem = curr_sum//10
      
    p1 -= 1
    p2 -= 1

  
  while p1 > 0:
    if rem != 0:
      res.insert(0, a[p1]+rem)
    else:
      res.insert(0, a[p1])
    p1 =- 1
      
  while p2 > 0:
    if rem != 0:
      res.insert(0, a[p1]+rem)
    else:
      res.insert(0, a[p1])
    p2 =- 1

  return res     

a = [4,5,1]
b = [3,4,5]

print(findArraySum(a, len(a), b, len(b)))