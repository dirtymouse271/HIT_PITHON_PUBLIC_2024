n = -1
tong = 0
while n<=0:
    n = int(input("nhap so nguyen duong n: "))
while n>0:
    du = n % 10
    tong += du
    n //= 10
print("tong cac chu so cua n la: ",tong)
