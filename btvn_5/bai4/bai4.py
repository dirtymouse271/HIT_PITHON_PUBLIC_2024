CONFIG = {
    'n': 1500,
    'm': 2,
    'CLUSTERS': 3,
    'ITER': 10000,
    'METHOD': 'FCM',
    'MEASURE': 'EUCLIDEAN',
    'YEARS': 51,
    }
print(CONFIG)
CONFIG['MEASURE'] = 'MANHATAN'
print(CONFIG)
print(CONFIG['METHOD'])
CONFIG['LOSS FUNCTION'] = 'NORM_2'
print(CONFIG)
CONFIG.pop('YEARS')
print(CONFIG)
S = input()
if S in CONFIG.values():
    print('YES')
else:print('NO')
set1 = set()
for i in CONFIG.values():
    set1.add(i)
print(set1)
list1 = []
for i in CONFIG.values():
    list1.append(i)
print(list1)
