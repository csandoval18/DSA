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

def fairCandySwap(aliceSizes: [int], bobSizes: [int]) -> [int]:
  aliceSum, bobSum = 0, 0
  for i in range(len(aliceSizes)):
    aliceSum += aliceSizes[i]
  
  for j in range(len(bobSizes)):
    bobSum += bobSizes[j]
  
  diff = abs(aliceSum-bobSum)
  if aliceSum == bobSum:
    return [aliceSum, bobSum]
  elif aliceSum < bobSum:
    return [aliceSum+diff, bobSum-diff]
  else:
    return [aliceSum-diff, bobSum+diff]
    