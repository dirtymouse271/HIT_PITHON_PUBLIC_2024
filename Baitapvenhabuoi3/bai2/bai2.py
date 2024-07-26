print("Nhập số phần tử của list: ")
k = int(input())
print("Nhập các phần tử: ")
a = [int(input()) for _ in range(k)]
print("Nhập số dòng của ma trận: ")
n = int(input())
print("Nhập số cột của ma trận ")
m = int(input())
if n*m > k:
    print("NO")
else:
    B = []
    index = 0
    for i in range(n):
        hang = []
        for j in range(m):
            hang.append(a[index])
            index += 1
        B.append(hang)
    for hang in B:
        print(hang)

