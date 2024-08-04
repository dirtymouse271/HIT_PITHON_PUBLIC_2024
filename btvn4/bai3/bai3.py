n, m = map(int, input().split())
S = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happy = 0
for i in S:
    if i in A:
        happy+=1
    elif i in B:
        happy-=1
print(happy)