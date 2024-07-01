from gettext import find


class UnionFindLinear: # Linear complexity methods of union find (inefficient)
  def __init__(self, size) -> None:
    self.parent = list(range(size))
    self.rank = [1] * size
    
  def find(self, u: int):
    if self.parent[u] == u:
      return u
    return find(self.parent[u])
      