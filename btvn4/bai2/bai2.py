set1 =set(input().split())
set2 =set(input().split())
if(set1.intersection(set2)):
    print("Y")
else: print("N")
print(set1.intersection(set2))
print(set1.difference(set2))