from typing import List

# You are given 0 indexed string source and target, both of length n
# and consisting of lowercase Ennglish chars. You are also given two 0-indexed
# string arrays original and changed, and an integer array cost, where cost[i]
# represents the cost of converting the string original[i] to the string changed[i]

class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    n = len(source)
    