#Preeyanee Srimuang
#6809610220
#29

import math
a = int(input())
b = int(input())
c = int(input())
x1 = ((-b)-math.sqrt((b**2)-4*a*c))/2*a
x2 = ((-b)+math.sqrt((b**2)-4*a*c))/2*a
print("%.3f"%x1 , "%.3f"%x2)
