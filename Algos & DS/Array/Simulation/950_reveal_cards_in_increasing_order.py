from collections import deque

def deckRevealedIncreasing(deck):
  # Step 1: Sort the deck to know the target order
  sorted_deck = sorted(deck, reverse=True)
  
  # Step 2: Use a deque to simulate the reverse process
  queue = deque()
  
  # Reverse process: place cards from sorted in their correct position.
  for card in sorted_deck:
    # If there's already a card in the queue, move the top one to the bottom.
    if queue:
      queue.append(queue.pop())
      
    # Place the current card in its "final" position (which is the top for our reverse simulation).
    queue.appendleft(card)
    
  # The queue now represents the initial order to achieve the desired reveal process.
  return list(queue)