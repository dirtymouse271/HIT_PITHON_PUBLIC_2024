n = int(input().strip())
a = [input().strip() for _ in range(n)]
b = tuple(a)
count = sum(1 for item in b if item.isdigit())
print(b)
print(count)
