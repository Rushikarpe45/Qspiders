# Modules:
# 1) math module:
import math
math.sqrt(8)
2.8284271247461903
math.factorial(5)
120
math.lcm(2,8,16)
16
math.gcd(5,10)
5
math.pi
3.141592653589793
# 2) random module:
import random
random.random()
0.32204350635189194
random.random()
0.5353827657444836
random.randint(1,100)
90
random.randint(1,100)
85
random.randint(1,100)
11
random.randint(1,100)
50
random.choice('Modules')
'M'
random.choice('Modules')
's'
random.choice('Modules')
'u'
random.shuffle([10,20,30,40])
a = [10,20,30,40]
random.shuffle([10,20,30,40])
a
[10, 20, 30, 40]
random.shuffle(a)
a
[10, 20, 40, 30]
a
[10, 20, 40, 30]
random.shuffle(a)
a
[20, 10, 30, 40]
random.shuffle(a)
a
[20, 10, 40, 30]
# 3) time module:
import time
time.time()
1744036083.114272
time.sleep(5)
# 4) calendar module

import calendar
calendar.calendar(2025)
calendar.month(2025,12)
calendar.month(2025,12)
' December 2025\nMo Tu We Th Fr Sa Su\n 1 2 3 4 5 6 7\n 8 9 10 11 12 13 14\n15 16 17 18 19 20 21\n22'