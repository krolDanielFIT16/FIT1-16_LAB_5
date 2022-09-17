def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


Mx = float(input("Mx = "))
My = float(input("My = "))
Ax = float(input("Ax = "))
Ay = float(input("Ay = "))
Bx = float(input("Bx = "))
By = float(input("By = "))
Cx = float(input("Cx = "))
Cy = float(input("Cy = "))


AM = dist(Ax, Ay, Mx, My)
BM = dist(Bx, By, Mx, My)
CM = dist(Cx, Cy, Mx, My)

if (AM < BM) and (AM < CM):
    print("A")
elif (BM < AM) and (BM < CM):
    print("B")
elif (CM < AM) and (CM < BM):
    print("C")
