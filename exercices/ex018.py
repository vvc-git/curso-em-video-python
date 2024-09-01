from math import sin, cos, tan, pi
a = float(input('Type the angle(º): '))
print('The sine of {} is {:.2f}; the cosine is {:.2f}; and the tangent is {:.2f}'.format(a, sin((pi*a)/180), cos((pi*a)/180), tan((pi*a)/180)))
