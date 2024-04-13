from collections import deque

def deckRevealedIncreasing(deck):
  deck.sort()
  n = len(deck)
  res = [0]*n
  queue = deque(range(n)) # Start a queue from range(0, n) symbolizing the indices
  # [0,1,2,3,4,5]
  
  for num in deck:
    # First we need to take the first num, then skip the next index
    i = queue.popleft() # Get the index
    res[i] = num # Set value in res to current sorted value
    
    if queue:
      queue.append(queue.popleft()) # Skip the next index
  
  return res
    
