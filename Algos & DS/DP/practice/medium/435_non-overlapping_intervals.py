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
      
    

intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping