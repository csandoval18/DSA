# Pair Sum

# You are given an arr consisting of n distinct ints arranged in 
# ascending order. You are given an int 'target'. 

# Your task is to count all the distict pairs in arr such that their
# sum is equal to 'target'

# Note:
# 1. Pair (x,y) and pair (y,x) are considered to be the same pair.
# 2. If there exists no such pair with sum equals to 'target' return -1

# [1,2,3,4,5]
# t = 6

def pairSum(arr, n, target):
  a, b = 0, n-1
  cnt = 0
  
  while a != b:
    s = arr[a] + arr[b]
    
    if s == target:
      cnt += 1
      b -= 1
    elif s < target:
      a += 1
    else:
      b -= 1
  return cnt if cnt > 0 else -1
    
arr = [1,2,3,4,5]
target = 6
print(pairSum(arr, len(arr), target))
