from ast import List

def countStudents(students: List[int], sandwiches: List[int]) -> int:
  student_queue = deque(students)
  sandwich_stack = deque(sandwiches)
  
  while student_queue and sandwich_stack:
    if student_queue[0] == sandwich_stack[0]:
      student_queue.popleft()
      sandwich_stack.popleft()
    else:
      student_queue.append(student_queue.popleft()) # student goes to the end of the line
  