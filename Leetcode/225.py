# Python program to demonstrate
# stack implementation using a linked list.
# node class
 
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
 

class MyStack(object):
    def __init__(self):
      self.head = Node()

    def push(self, x):
      """
      :type x: int
      :rtype: None
      """

    def pop(self):
      """
      :rtype: int
      """
      if self.isEmpty():
        raise Exception("Popping from an empty stack")
      remove = self.head.next

    def top(self):
      """
      :rtype: int
      """

    def empty(self):
      """
      :rtype: bool
      """

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()