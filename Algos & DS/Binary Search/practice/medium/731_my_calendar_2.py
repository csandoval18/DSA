class MyCalendarTwo:
  def __init__(self):
    self.calendar = []  # Stores the booked events
    self.overlaps = []  # Stores the double-booked events

  def book(self, start: int, end: int) -> bool:
    # Check if the new event would cause a triple booking
    for o_start, o_end in self.overlaps:
      if start < o_end and end > o_start:  # Overlap exists in overlaps
        return False
    
    # Check for overlaps with existing events
    for c_start, c_end in self.calendar:
      if start < c_end and end > c_start:  # Overlap with a calendar event
        # Record this overlap in overlaps
        self.overlaps.append((max(start, c_start), min(end, c_end)))
    
    # Add the new event to the calendar
    self.calendar.append((start, end))
    return True