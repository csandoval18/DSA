from collections import deque
from typing import List

# The problem "Minimum Multiplications to reach End" can be understood as 
# finding the shortest path in a weighted graph where the weights represent multiplication operations

# Given an array arr[] of size N and two integers start and end, find the 
# minimum number of multiplications needed to reach from start to end using 
# the elements of the array arr[] as multipliers. You can multiply start by any 
# element of arr[] any number of times to reach end.
 
class Solution:
  def minimum_multiplications(arr: List[int], start: int, end):
    # Create a queue for storing the numbers as a result of multiplication
    # of the numbers in the array and the start number.
    q = deque([(start, 0)])
    
    # Create a dist array to store the no. of multiplications to reach
    # a particular number from the start number.
    dist = [int(1e9)] * 100000
    dist[start] = 0
    mod = 100000
    
    # Multiply the start no. with each of numbers in the arr
    # until we get the end no.
    while q:
      node, steps = q.popleft()
      
      for it in arr:
        num = (it * node) % mod
        
        # If the no. of multiplications are less than before
        # in order to reach a number, we update the dist array.
        if steps + 1 < dist[num]:
          dist[num] = steps + 1
          
          # Whenever we reach the end number
          # return the calculated steps
          if num == end:
            return steps + 1
          q.append((num, steps + 1))
          
    # If the end no. is unattainable.
    return -1
  
start = 3 
end = 30
arr = [2, 5, 7]
s = Solution()
print(s.minimumMultiplications(arr, start, end))