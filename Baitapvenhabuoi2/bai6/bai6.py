n= int(input("nhap so n: "))
sohoanhao = []
for x in range(1,n+1):
    tong = 0
    for i in range(1,x):
        if x%i==0:
            tong+=i
    if tong == x:
        sohoanhao.append(x)
print(f"{sohoanhao}")