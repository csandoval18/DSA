from typing import Counter, List

class Solution:
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
      return False
    
    card_count = Counter(hand) # Count the frequency of each card
    sorted_cards = sorted(card_count.keys()) # Short the unique cards
    
    # Attempt to form groups
    for card in sorted_cards:
      # If there are any of this card left to be used in a group
      while card_count[card] > 0:
        # Try to form a group starting with this card
        for i in range(groupSize):
          if card_count[card+i] > 0:
            card_count[card+i] -= 1
          else:
            # If we cant form a group, return False
            return False
            
    # If all cards can be grouped correctly, return True
    return True
    