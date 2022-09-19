from math import *


def func(x):
    if x > 7:
        return 2.27*pow(e, 4*x+1)+3
    elif 0.5 < x <= 7:
        return 0.64*pow(x, x+0.1)
    else:
        return log(fabs(x - e ** x), e)
    
print(func(float(input("x = "))))
