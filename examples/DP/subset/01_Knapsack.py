def f(idx):
  if idx == 0:
    return 
    
  print(idx)
  f(idx-1)

f(10)


# bag weight = 8
# weights => 3  4  5
# vals    => 30 50 60

# can't pick 4, 5 because 4+5=9 > 8 bag weight

