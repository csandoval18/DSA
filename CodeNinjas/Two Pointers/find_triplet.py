def findTriplet(arr: [int], n: int) -> bool:
  arr.sort()
  for i in range(n-1,-1,-1):
    l, r = 0, i-1
    
    while l<r:
      