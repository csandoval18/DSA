import itertools

# Combinations of a list 

data = ['A', 'B', 'C']
combinations = itertools.combinations(data, 2)

for combo in combinations:
  print(combo)

# ('A', 'B')
# ('A', 'C')
# ('B', 'C')

# Combinations of a string

data = 'ABC'
combinations = itertools.combinations(data, 2)

for combo in combinations:
  print(''.join(combo))

# AB
# AC
# BC

# Combinations with Repetition

data = ['A', 'B', 'C']
combinations = itertools.combinations_with_replacement(data, 2)

for combo in combinations:
  print(combo)

# ('A', 'A')
# ('A', 'B')
# ('A', 'C')
# ('B', 'B')
# ('B', 'C')
# ('C', 'C')

# Function to generate combinations:
def combinations(iterable, r):
  pool = tuple(iterable)
  n = len(pool)
  
  if r > n:
      return
  
  indices = list(range(r))
  yield tuple(pool[i] for i in indices)
  
  while True:
    for i in reversed(range(r)):
      if indices[i] != i + n - r:
        break
    else:
      return
    indices[i] += 1
    for j in range(i + 1, r):
      indices[j] = indices[j - 1] + 1
    yield tuple(pool[i] for i in indices)

# Usage example
data = ['A', 'B', 'C']
for combo in combinations(data, 2):
  print(combo)