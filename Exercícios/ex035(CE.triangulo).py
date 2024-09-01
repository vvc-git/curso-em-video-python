a = float(input('\nType the length of the first line: '))
b = float(input('Type the length of the second line: '))
c = float(input('Type the length of the third line: '))
print(20*'=*=')
if a<b+c and b<a+b and c<a+b:
   print("Okay! you can make a triangle.")
else:
   print("Ops! You can't make a triangle.")



