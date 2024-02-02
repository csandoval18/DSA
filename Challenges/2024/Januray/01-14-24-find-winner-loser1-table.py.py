from collections import Counter
from typing import List

def findWinners(matches: List[List[int]]) -> List[List[int]]:
  lostCount = {}
  
  for winner, loser in matches:
    lostCount[winner] = lostCount.get(winner, 0)
    lostCount[loser] = lostCount.get(loser, 0)+1

  winners = [i for i in lostCount if lostCount[i] == 0] 
  lost_one = [i for i in lostCount if lostCount[i] == 1]

  return [sorted(winners), sorted(lost_one)]