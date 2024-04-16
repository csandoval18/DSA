from ast import List
from collections import deque

def countStudents(students: List[int], sandwiches: List[int]) -> int:
  student_queue = deque(students)
  sandwich_stack = deque(sandwiches)
  
  while student_queue and sandwich_stack:
    if student_queue[0] == sandwich_stack[0]:
      student_queue.popleft() # Student takes sandwich and leaves queue
      sandwich_stack.popleft() # sandwich is removed from stack
    else:
      student_queue.append(student_queue.popleft()) # student goes to the end of the line
  
  
    # Manual check to see if any student can eat the sandwich at the front
    found_match = False
    for student in student_queue:
      if student == sandwich_stack[0]:
        found_match = True
        break
    
    if not found_match:
      break
      
  return len(student_queue)