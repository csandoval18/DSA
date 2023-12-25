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
    if arr[a] + arr[b] == target:
      cnt += 1
    