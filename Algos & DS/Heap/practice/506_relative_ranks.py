from functools import cmp_to_key
import heapq
from typing import List

# Easy (max heap, sorting)

# Method 1: Max Heap 
# Using max heap by turning python default min heap into a max heap by using 
def find_relative_ranks(score: List[int]):
  # Create a max heap (sing negative values for a max heap)
  heap = [(-s, i) for i, s in enumerate(score)]
  heapq.heapify(heap)
  
  # Create a result array 
  res = [""] * len(score)
  
  # Extract elements from heap and assign ranks
  for rank in range(1, len(score) + 1):
    # Pop the largest element (most negative in our max heap)
    neg_score, i = heapq.heappop(heap)
    if rank == 1:
      res[i] = "Gold Medal"
    elif rank == 2:
      res[i] = "Silver Medal"
    elif rank == 3:
      res[i] = "Bronze Medal"
    else:
      res[i] = str(rank)
    
  return res

# Method 2: Sorting
def find_relative_ranks(score: List[int]):
  # Create a list of tuples (index, score) to keep track of the original indices
  enumerated_scores = list(enumerate(score))
  
  # Custom comparator function to sort by score in descending order
  def compare(a, b):
    return b[1] - a[1]

  enumerated_scores.sort(key=cmp_to_key(compare)) # Sort the enumerated scores using the custom comparator
  result = [""] * len(score) # Create a result array with the same length as the input
  
  # Assign medals or ranks based on the sorted order
  for i, (index, score) in enumerate(enumerated_scores):
      if i == 0:
          result[index] = "Gold Medal"
      elif i == 1:
          result[index] = "Silver Medal"
      elif i == 2:
          result[index] = "Bronze Medal"
      else:
          result[index] = str(i + 1)
  
  return result
  
# Using Hash Maps
class Solution:
  def findRelativeRanks(self, score: List[int]) -> List[str]:
    sortedscore = sorted(score, reverse=True)
    # print(sortedscore)
    mapping = {}
    medals = 0
    for i in range(len(sortedscore)):
      if medals == 0:
        mapping[sortedscore[i]] = "Gold Medal"
        medals += 1
      elif medals == 1:
        mapping[sortedscore[i]] = "Silver Medal"
        medals += 1
      elif medals == 2:
        mapping[sortedscore[i]] = "Bronze Medal"
        medals += 1
      else:
        mapping[sortedscore[i]] = str(i+1)
  # print(mapping)
    ans = []
    for s in score:
      ans.append(mapping[s])
    return ans


def findRelativeRanks(self, score: List[int]) -> List[str]:
  arr = score.copy()
  arr.sort(reverse = True)
  dict = {}
  l=[]
  for i in range(len(score)):
    if arr[i] not in dict:
        if i == 0:
            dict[arr[i]]="Gold Medal"
        elif i == 1:
            dict[arr[i]]="Silver Medal"
        elif i == 2:
            dict[arr[i]]="Bronze Medal"
        else:
          dict[arr[i]]=str(i+1)
  for k in score:
    l.append(dict[k])
  return l

def findRelativeRanksHM(score: List[int]) -> List[str]:
  arr = score[:]
  arr.sort(reverse = True)
  print(arr)
  hm = {}
  res = []

  for i in range(len(score)):
    if arr[i] not in hm:
      if i == 0:
        hm[arr[i]] = 'Gold Medal'
      elif i == 1:
        hm[arr[i]] = 'Silver Medal'
      elif i == 2:
        hm[arr[i]] = 'Bronze Medal'
      else:
        hm[arr[i]] = str(i+1)
  for k in score:
    res.append(hm[k])
  return res

score = [5,4,3,2,1]
print(findRelativeRanksHM(score))