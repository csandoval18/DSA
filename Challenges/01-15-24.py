import random

def __init__(self):
  self.values = []
  self.hm = {}
  
def insert(self, val: int) -> bool:
  if val in self.hm:
    return False
  self.values.append(val)
  self.hm[val] = len(self.values)-1 
  return True
    
def remove(self, val: int) -> bool:
  if val not in self.hm:
    return False
    
  last_val = self.values[-1]
  key_cnt = self.hm[val]
  self.values[key_cnt], self.values[-1] = self.values[-1], self.values[key_cnt]
  self.hm[last_val] = key_cnt
  self.values.pop()
  del self.hm[val]
  
  return True
  
def getRandom(self) -> int:
  return random.choice(self.values)
  
  