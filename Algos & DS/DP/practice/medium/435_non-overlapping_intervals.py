from typing import List

'''
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the
minimum number of intervals you need to remove to make the rest of the intervals non-
overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2]
and [2, 3] are non-overlapping.
'''

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1]) # Sort by end times
    
    def helper(i: int, prev_end: int) -> int: 
      if i == len(intervals):
        return 0
      
      exclude = helper(i + 1, prev_end) # Option 1: Exclude the current interval
      
      include = float('inf') # Option 2: Include the current interval if it doesnt overlap
      if intervals[i][0] >= prev_end:
        include = helper(i+1, intervals[i][1])
      
      # Return the min removals
      return min(exclude, 1 + include)
      
    
class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1]) 
    memo = {}
    
    def helper(i: int, prev_end: int) -> int:
      if i == len(intervals):
        return 0
      
      exclude = helper(i+1, prev_end)
      include = float('inf')
      if intervals[i][0] >= prev_end:
        include = helper(i+1, intervals[i][1])
        
      # Memoize and return the result
      memo[(i, prev_end)] = min(exclude, 1 + include)
      return memo[(i, prev_end)]
    return helper(0, float('-inf'))
      

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1]) # Sort by end times
    n = len(intervals)
    dp = [0] * n # dp[i] stores the min removals for intervals[0..i]
    
    for i in range(1, n):
      if intervals[i][0] < intervals[i-1][1]: # Overlapping
        dp[i] = dp[i-1] + 1
      else:
        dp[i] = dp[i-1] # No overlap, carry forward
    return dp[-1]
        

intervals = [[1,2],[2,3],[1,3],[3,4]]
# [1,2],[2,3],[1,3],[3,4]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping

