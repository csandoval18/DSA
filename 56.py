#56 Merge Overlapping Subintervals

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# Brute Force O(n log n) + O(2n)
def mergeOverlappingIntervals(intervals):
  n = len(intervals)
  ans = []
  
  # 1. Sort the closer intervals [X, 0]
  intervals.sort()
  
  for i in range(n):
    # 2. Select one interval 
    # [start,end] format
    start, end = intervals[i][0], intervals[i][1]
    
    # Skip all the merged intervals:
    if ans and end <= ans[-1][1]:
      continue
      
    for j in range(n):
      # Each row start
      if intervals[j][0] <= end:
        end = max(end, intervals[j][1])
      else:
        break
      
    ans.append([start, end])

  return ans


# Optimal O(n)
def mergeOverlappingIntervals(intervals):
  n = len(intervals)
  intervals.sort()
  res = []
  
  for i in range(n):
    if res or intervals[i][0] > res[-1][1]:
      
  
  return res
  
      
  