from typing import List


class Solution:
  def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()
    moves = 0
    
    for i in range(len(seats)):
      if seats[i] == students[i]:
        continue
        
      moves += abs(seats[i] - students[i])
      
    return moves
        
        
seats = [3,1,5]
students = [2,7,4]
s = Solution()
print(s.minMovesToSeat(seats, students))

# 1 3 5
# 2 4 7

# 2 - 1 = 1
# 4 - 3 = 1
# 7 - 5 = 2

# 1 4 5 9 seats 
# 1 2 3 6 students
# 0 2 2 3 moves