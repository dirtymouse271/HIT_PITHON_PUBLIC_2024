n = int(input("nhap so n: "))
tong = 0
for x in range(1,n+1):
    if x % 2 != 0:
        tong += x
    else: tong -=x
print(tong)
    

