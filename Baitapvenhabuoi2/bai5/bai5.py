n = int(input("nhap so n: "))
amstrong=[]
for x in range(1,n+1):
    phu = x
    tong = 0
    while phu > 0:
        du=phu % 10
        tong += du**3
        phu //= 10
    if tong == x:
        amstrong.append(x)
print(f"{amstrong}")