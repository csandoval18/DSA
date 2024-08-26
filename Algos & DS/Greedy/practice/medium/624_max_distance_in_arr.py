from typing import List


class Solution:
  def maxDistance(self, arrays: List[List[int]]) -> int:
    minima = arrays[0][0]
    maxima = arrays[0][-1]
    max_dist = 0
    for i in range(1, len(arrays)):
      curr_min = arrays[i][0] # Remember each array is sorted so curr min is at start
      curr_max = arrays[i][-1] # and curr max is at the end of the curr list

      # Calculate distance using the current array's values
      max_dist = max(max_dist, abs(curr_max - minima), abs(maxima - curr_min))
      
      # Update min_val and max_val
      minima = min(minima, curr_min)
      maxima = max(maxima, curr_max)
    
    return max_dist