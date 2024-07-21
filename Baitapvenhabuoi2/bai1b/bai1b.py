n=-1
uoc=0
while n<0:
    n= int(input("nhap so nguyen duong n: "))
for x in range(1,n+1):
    if n%x==0:
        uoc+=x
print("tong cac uoc cua so n la: ",uoc)
    