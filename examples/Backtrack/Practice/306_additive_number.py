from typing import List

def isAdditiveNumber(num: str) -> bool:
  n = len(num)
  def backtrack(start: int, path: List[int]):
    if start == n:
      return len(path) >= 3 # Check if at least three numbers are found
    
    for end in range(start+1, n+1): # Traversing ending pointer through string until a number is equal to path[n-1] + path[n-2]
      if num[start] == '0' and end > start+1: # Leading zero is not allowed except except for single digit
        break
      
      nextNum = int(num[start:end])
      if len(path) < 2 or nextNum == path[-1] + path[-2]:
        # If we find a number range that matches the conditions then we can backtrack to repeat the search in the next section of the arr 
        # starting from the ending pointer
        if backtrack(end, path + [nextNum]):
          return True
    return False
    
  return backtrack(0, [])
        
      
        
num = "112358"
# Output: True
print(isAdditiveNumber(num))

#                   backtrack(0, [])
#                  /                 \
# backtrack(1, [1])                  backtrack(1, [])
#  /         \                          /           \
# backtrack(2, [1, 1])              backtrack(2, [1])
#  /         \                          /           \
# backtrack(3, [1, 1, 2])          backtrack(3, [1, 1])
#  /         \                          /           \
# backtrack(5, [1, 1, 2, 3])      backtrack(5, [1, 1, 2])
#                                     /
#                         backtrack(6, [1, 1, 2, 3, 5])
#                          /              \
#           backtrack(7, [1, 1, 2, 3, 5])    backtrack(7, [1, 1, 2, 3, 5, 8])
