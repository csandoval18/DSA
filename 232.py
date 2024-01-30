# 232. Implement Queue using Stacks

class MyQueue:
  def __init__(self):
    self.queue = []
    self.st = []
    
  def push(self, x: int) -> None:
    self.queue.append(x)

  def pop(self) -> int:
    x = self.queue[0]
    self.queue  = self.queue[1:]
    return x

  def peek(self) -> int:
    return self.queue[0]

  def empty(self) -> bool:
    return len(self.queue) == 0 
    

queue = MyQueue()
queue.push(1)
print(queue.peek())
queue.push(2)
print(queue.peek())
queue.push(3)
print(queue.peek())
queue.pop()
print(queue.peek())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
print()
arr = [1,2,3]
print(arr[1:])