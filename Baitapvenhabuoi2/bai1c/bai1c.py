a=-1
b=-1
c=-1
while a<0:
    a=int(input("nhap canh a: "))
while b<0:
    b=int(input("nhap canh b: "))
while c<0:
    c=int(input("nhap canh c: "))
if a+b>c and a+c>b and b+c>a:
    print("Day la tam giac")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("Va la tam giac vuong")
    elif a == b or b == c or c == a:
        print("Va la tam giac can")
    elif a == b == c:
        print("Va la tam giac deu")
    elif a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
        print("Va la tam giac nhon")
    else: print("Va la tam giac tu") 

