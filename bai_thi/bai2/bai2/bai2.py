n = -1
while n<1 and n >1000:
    n = int(input())
buoc = 0
for i in range(n):
    buoc = n/3
    if n%3 != 0:
        buoc+=1
print(buoc)
