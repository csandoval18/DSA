from heapq import heappop, heappush
from typing import List


class Solution:
  def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    # Step 1: Initialize the ugly number list and heap
    ugly = [1]
    pq = []
    
    # Step 2: Initialize heap with each prime number, their current pointer (index), and product
    for prime in primes:
      heappush(pq, (prime, prime, 0)) # (product, prime, index of ugly number)
    
    # Step 3: Generate super ugly numbers up to nth
    for i in range(1, n):
      # Step 4: Get the smallest number from the heap (next ugly number)
      next_ugly, prime, index = pq[0]
      ugly.append(next_ugly)
      
      # Step 5: Ensure duplicates are not added by comparing with the last added ugly number
      while pq and pq[0][0] == next_ugly:
        _, prime, idx = heappop(pq)
        heappush(pq, (prime * ugly[idx+1]), prime, idx+1)
    
    # Step 6: Return the nth super ugly number
    return ugly[-1]