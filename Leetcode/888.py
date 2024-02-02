# Fair Candy Swap

# Alice and Bob have diff total nums of candies. You are given 2 int arrs aliceSize
# & bobSizes where aliceSizes[i] is the num of candies of the ith obx of candy that 
# Alice has and bobSizes[j] is the num of candies of the jth box of candy
# that Bob has.

# Since they are friends, they would like to exchange one candy box each so that after 
# the exchange, they both have the same total amount of candy. The total amount of candy 
# a person has is the sum of the number of candies in each box they have.

# Return an integer array answer where answer[0] is the number of candies in the box that 
# Alice must exchange, and answer[1] is the number of candies in the box that Bob must 
# exchange. If there are multiple answers, you may return any one of them. 
# It is guaranteed that at least one answer exists.

# ans[0] = # of candy Alice must exachange
# ans[1] = # of candy Bob must exchange

# Ex:
# aliceSizes = [1,1], bobSizes = [2,2]
# We need to make the arrays be equal, so we can pass a 1 to bobSizes and 2 to aliceSizes
# Output: 
# [1,2]

# BF
def fairCandySwap(aliceSizes: [int], bobSizes: [int]) -> [int]:
  diff = sum(aliceSizes) - sum(bobSizes)
  # Check if diff is uneven
  if diff%2 != 0:
    return [-1, -1]
  
  a, b = 0, 0
  while a < len(aliceSizes):
    while b < len(bobSizes):
      if aliceSizes[a]-bobSizes[b] == diff // 2:
        return [bobSizes[b], aliceSizes[a]]
      b += 1
    a += 1
    b = 0

def fairCandySwapBS(aliceSizes, bobSizes):
  diff = sum(aliceSizes)-sum(bobSizes)
  if diff%2 != 0:
    return [-1, -1]
  t = diff//2
  l, r = 0, len(bobSizes)-1
  
  while l<=r:
    m = (l+r)//2
    if bobSizes[m] >= t:
      r = m-1
    else:
      l = m+1
  
  # Check for valid swap: handle all edge cases
  if aliceSizes[l] == t or (aliceSizes[0] == aliceSizes[l] and aliceSizes[0] == t):
    return [bobSizes[r], aliceSizes[l]]
  elif len(aliceSizes) == 2 and aliceSizes[0] == bobSizes[0]:  # Handle scenario of identical and unique candies
    return [bobSizes[1], aliceSizes[1]]
  else:
    return [-1, -1]
  
    
aliceSizes = [1,1]
bobSizes= [2,2]
print(fairCandySwapBS(aliceSizes, bobSizes))