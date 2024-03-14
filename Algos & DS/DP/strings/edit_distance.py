# 72. Edit Distance
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

#     i
# horse
# ros
#   j

# if word1[i] == word2[j]:
#   return 0 + f(i-1, j-1)

# Insert: 1 + f(i, j-1) 
# Delete: 1 + f(i-1, j)
# Replace: 1 + f(i-1, j-1)

# Base case => when its over
# 2 scenarios: word1 gets exhausted, word2 gets exhausted
# ------------------------------------------

# if word1 gets exhausted we return j+1 since we will need j+1 insert operations to input the remaining chars in word2
# Ex: f(-1, 1) => j+1 = 2 inserts 

# i
# -1 0 1 2 3 4 
#    h o r s e
# r o s
# 0 1 2
#   j
# insert('o'), insert('r') 

# if i < 0: return j+1

# ------------------------------------------

# if word2 gets exahusted we return i+1 since we will need to delete the remaining chars in word1
# Ex: f(2, -1) => i+1 = 3 deletes

#     i
# 0 1 2 3 4
# h o r s e

#    r o s 
# -1 0 1 2
#  j
# del('r'), del('o'), del('h')

# if j < 0: return i+1

# Recursion TC => Exponential
from typing import List


def minDistanceRec(word1: str, word2: str) -> int:
  def f(i: int, j: int) -> int:
    if i < 0:
      return j+1
    if j < 0:
      return i+1
      
    if word1[i] == word2[j]:
      return f(i-1, j-1)
    
    return 1 + min(f(i-1, j), f(i, j-1), f(i-1, j-1))
  
  n, m = len(word1), len(word2)
  return f(n-1, m-1)

# TC: O(n*m), SC: O(n*m)
def minDistanceMemo(word1: str, word2: str) -> int:
  def f(i: int, j: int, dp: List[List[int]]) -> int:
    if i < 0:
      return j+1
    if j < 0:
      return i+1
    
    if dp[i][j] != -1:
      return dp[i][j]
      
    if word1[i] == word2[j]:
      return f(i-1, j-1, dp)
    
    return 1 + min(f(i-1, j, dp), f(i, j-1, dp), f(i-1, j-1, dp))
   
  n, m = len(word1), len(word2)
  dp = [[-1]*(m+1) for _ in range(n+1)]
  return f(n-1, m-1, dp)
  
def minDistanceMemo2(word1: str, word2: str) -> int:
  def f(i: int, j: int, dp: List[List[int]]) -> int:
    if i == 0:
      return j
    if j == 0:
      return i
    
    if dp[i][j] != -1:
      return dp[i][j]
      
    if word1[i-1] == word2[j-1]:
      return f(i-1, j-1, dp)
    
    return 1 + min(f(i-1, j, dp), f(i, j-1, dp), f(i-1, j-1, dp))
   
  n, m = len(word1), len(word2)
  dp = [[-1]*(m+1) for _ in range(n+1)]
  return f(n-1, m-1, dp)

def minDistanceTab(word1: str, word2: str) -> int:
  n, m = len(word1), len(word2)
  dp = [[0]*(m+1) for _ in range(n+1)]
  
  for i in range(n+1):
    dp[i][0] = i
    
  for j in range(m+1):
    dp[0][j] = j
    
  for i in range(1, n+1):
    for j in range(1, m+1):
      if word1[i-1] == word2[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
  
  for i in range(n):
    print(dp[i])
  return dp[n][m]

def minDistanceSO(word1: str, word2: str) -> int:
  n, m = len(word1), len(word2)
  prev, curr = [0]*(m+1), [0]*(m+1)
  
  # for i in range(n+1):
  #   dp[i][0] = i
    
  for j in range(m+1):
    prev[j] = j
    
  for i in range(1, n+1):
    curr[0] = i
    for j in range(1, m+1):
      if word1[i-1] == word2[j-1]:
        curr[j] = prev[j-1]
      else:
        curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
      
    prev = curr[:]
  
  return prev[m]
  
  
word1 = "horse"
word2 = "ros"
print(minDistanceRec(word1, word2))
print(minDistanceMemo(word1, word2))
print(minDistanceMemo2(word1, word2))
print(minDistanceTab(word1, word2))
print(minDistanceSO(word1, word2))
