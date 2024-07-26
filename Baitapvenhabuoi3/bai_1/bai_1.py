import math
print("Nhập số phần tử của list: ")
n = int(input())
print("Nhập list: ")
list_n =[int(input()) for _ in range(n)]
countt = 0
print("Nhập x: ")
x = int(input())    
for i in range(n):
    if list_n[i] == x:
        countt+=1
        i+=1
print('số phần tử {x} trong list là: ',countt)
list_n[2:8] = [8, 5, 4, 0, 1, 3]
print(max(list_n))
print(min(list_n))
print("Nhập số y: ")
y = int(input())
list_n.insert(0,y)
count1 = 0
count2 = 0
for i in range(len(list_n)-1):
    if list_n[i] > list_n[i+1]:
        count1+=1
    elif list_n[i+1] > list_n[i]:
        count2+=1
if count1 == len(list_n)-1:
    print("Tăng")   
elif count2 == len(list_n)-1:
    print("giảm")
else:print("NO")
list_m = []
list_m = [sum(list_n[:i]) for i in range(1,n+1)]
print(list_m)
list_o = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
for i in range(len(list_o)):
    list_o[i] = abs(list_o[i])
list_o = sorted(list_o)
print(list_o)

