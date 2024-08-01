from typing import List

# * Knapsack style DP problem

# You are given an array books where books[i] = [width, height] indicates the thickness and height of the ith book.
# You are also given an integer shelfWidth. 

# We want to place these books in order onto bookcase selves that have a total width shelfWidth.

# We choose some of the to place on this shelf such that the sum of their thickness is
# less than or equal to shelfWidth, then build another level of the shelf of the bookcase so
# that the total height of the bookcase has increased by the maximum height of the books we
# just put down. We repeat this process until there are no more books to place.

# Note that at each step of the above process, the order of the books we place is the same
# order as the given sequence of books.

# For example, if we have an ordered list of 5 books, we might place the first and second
# book onto the first shelf, the third book on the second shelf, and the fourth and fith book on the last shelf.

# Return the minimun possible height that the total bookshelf can be after placing shelves in this manner.

class Solution:
  def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    n = len(books)
    dp = [float('inf')] * (n+1)
    dp[0] = 0 # Base case: no books, no height
    
    for i in range(1, n+1): # Iterate through each book to calculate the min heigh up to the ith book
      width = height = 0
      
      for j in range(i, 0, -1): # Iterate backwards to check books that can be placed on the current shelf
        width += books[j-1][0]
        
        if width > shelfWidth:
          break
          
        height = max(height, books[j-1][1])
        dp[i] = min(dp[i], dp[j-1] + height)
    
    return dp[n]

class Solution:
  def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    cache = {}
    
    def helper(i: int):
      if i == len(books):
        return 0
        
      if i in cache:
        return cache[i]
      
      curr_w = shelfWidth
      max_h = 0
      cache[i] = float('inf')
      
      for j in range(i, len(books)):
        w, h = books[j]
        
        if curr_w < w:
          break
        
        curr_w -= w
        max_h = max(max_h, h)
        cache[i] = min(cache[i], helper(j+1) + max_h)
      return 
      
    return helper(0)

class Solution:
  def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    n = len(books)
    dp = [0] * (n+1)
    
    for i in range(n-1,-1,-1):
      curr_w, max_h = shelfWidth, 0
      max_height = 0
      dp[i] = float('inf')
      
      for j in range(i, len(books)):
        w, h = books[j]
        
        if curr_w < w:
          break
        
        curr_w -= w
        max_h = max(max_h, h)
        dp[i] = min(dp[i], dp[j+1] + max_h)
        
    return dp[0]
      
      
    

books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
# Output: 6

# Explanation:
# The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
# Notice that book number 2 does not have to be on the first shelf.