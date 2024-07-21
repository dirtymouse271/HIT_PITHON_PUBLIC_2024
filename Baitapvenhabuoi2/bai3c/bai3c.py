import math
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
c = int(input("nhap so c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh vo so nghiem")
        else: print("phuong trinh vo nghiem")
    else: print("x = ",-c/b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("phuong trinh vo nghiem")
    elif delta == 0:
        print("phuong trinh co nghiem kep: ",-b/(2*a))
    else: 
        print("nghiem x1 = ",(-b+math.sqrt(delta))/(2*a))
        print("nghiem x2 = ",(-b-math.sqrt(delta))/(2*a))
