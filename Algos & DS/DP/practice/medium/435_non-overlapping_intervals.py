from typing import List

'''
Given an array of intervals intervals where intervals[i] = [start_i, end_i], 
return the min number of intervals you need to remove to make the rest of the intervals non-
overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2]
and [2, 3] are non-overlapping.
'''

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    n = len(intervals)
    intervals.sort()
    dp = [float('inf')] * (n+1)
    dp[n] = 0

    for i in reversed(range(n)):
      tgt = intervals[i][1]
      l, r = i+1, n
      
      while l < r:
        m = (l+r) // 2

        if intervals[m][0] < tgt:
          # intervals[m] cant be used after this, go higher
          l = m+1
        else:
          r = m
      dp[i] = min(dp[i+1]+1, dp[l]+(l-i-1))

    return dp[0]
        

intervals = [[1,2],[2,3],[1,3],[3,4]]
# [1,2],[2,3],[1,3],[3,4]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping
s = Solution()
print(s.eraseOverlapIntervals(intervals))