from math import *


def func(x):
    return (2.27*pow(e, 4*x+1)+3) if x > 7 else ((0.64*pow(x, x+0.1)) if (0.5 < x <= 7) else (log(fabs(x - e ** x), e)))


print(func(float(input("x = "))))
