import bisect


class MyCalendarBruteForce:

    def __init__(self):
      self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
      for s, e in self.calendar:
        # Check for overlap: if the new event starts before the end of the curr event
        # and ends after the start of the curr event
        if not (end <= s or start >= e):
          return False
        
      # If no conflict, add the event
      self.calendar.append((start, end))
      return True

class MyCalendarBinarySearch:
  def __init__(self):
    self.calendar = []
  
  def book(self, start: int, end: int) -> bool:
    # Find the insertion position for the new event using binary search
    i = bisect.bisect_right(self.calendar, (start, end))
    
    # Check for overlap with the prev event
    if i > 0 and self.calendar [i-1][1] > start:
      return False
    
    # Check for overlap with the next event
    if i < len(self.calendar) and self.calendar[i][0] < end:
      return False
    
    # If no overlap, insert the event at the correct position
    self.calendar.insert(i, (start, end))
    return True