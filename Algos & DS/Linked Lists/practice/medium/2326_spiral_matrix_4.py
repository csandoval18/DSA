from typing import List, Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
        
class Solution:
  def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    top, bottom = 0, m-1
    left, right = 0, n-1
    matrix = [[-1]*n for _ in range(m)]
    curr = head

    while left <= right and top <= bottom:
      for y in range(left, right+1):
        if curr:
          matrix[top][y] = curr.val
          curr = curr.next
        else:
          return matrix
      top += 1

      for x in range(top, bottom+1):
        if curr:
          matrix[x][right] = curr.val
          curr = curr.next
        else:
          return matrix
      right -= 1

      if top <= bottom:
        for y in range(right, left-1, -1):
          if curr:
            matrix[bottom][y] = curr.val
            curr = curr.next
          else:
            return matrix
          bottom -= 1

      if left <= right:
        for x in range(bottom, top-1, -1):
          if curr:
            matrix[x][left] = curr.val
            curr = curr.next
          else:
            return matrix
        left += 1
        
    return matrix