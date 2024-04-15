from ast import List

def countStudents(students: List[int], sandwiches: List[int]) -> int:
  student_queue = deque(students)
  sandwich_stack = deque(sandwiches)
  
  while student_queue and sandwich_stack:
    if student_queue[0] == sandwich_stack[0]:
      student_queue.popleft() # Student takes sandwich and leaves queue
      sandwich_stack.popleft() # sandwich is removed from stack
    else:
      student_queue.append(student_queue.popleft()) # student goes to the end of the line
  
    # Check if we are in a deadlock: if all remaining students do not want the sandwich at the front
    if all(s != sandwich_stack[0] for s in student_queue):
      break
  
  return len(student_queue)