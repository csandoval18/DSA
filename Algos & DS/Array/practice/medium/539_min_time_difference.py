from typing import List


class Solution:
  def findMinDifference(self, timePoints: List[str]) -> int:
    def timeToMinutes(time):
      hours, mins = map(int, time.split(":"))
      return hours * 60 + mins
    
    # Convert all time points to mins
    minsList = [timeToMinutes(time) for time in timePoints]
    # Sort the times in ascending order
    minsList.sort()
    # Initialize adjacent min difference as a large num
    res = float('inf')
    
    for i in range(1, len(minsList)):
      res = min(res, minsList[i] - minsList[i-1])
    
    # Check the wrap-around case (from last time to first time, across midnight)
    res = min(res, 1440 - (minsList[-1] - minsList[0]))
    return res
