#56 Merge Overlapping Subintervals

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# Brute Force
def mergeOverlappingIntervals(intervals):
  n = len(intervals)
  ans = []
  
  intervals.sort()
  
  for i in range(n):
    start, end = intervals[i][0], intervals[i][1]
    
    # Skip all the merged intervals:
    if ans and end <= ans[-1][1]
  