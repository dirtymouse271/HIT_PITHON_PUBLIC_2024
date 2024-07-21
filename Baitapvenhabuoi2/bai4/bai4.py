n=-1
while n <= 0:
    n = int(input("nhap n: "))
fibonacci = []
x = 0
while x<n:
    if x == 0:
        fibonacci.append(0)
    elif x == 1:
        fibonacci.append(1)
    else: 
        t = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(t)
    x+=1
print(f"{fibonacci}")