plus = 0
for c in range (1,3):
   weight = float(input('{}.How much do you weight? '.format(c)))
   plus = weight + plus
   if weight > plus:
      p1 = weight
