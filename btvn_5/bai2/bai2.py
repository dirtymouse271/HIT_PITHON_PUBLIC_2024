chuoiCanNhap = input()
countt = {}
for char in chuoiCanNhap:
    if char in countt:
        countt[char] += 1
    else:
        countt[char] = 1
for char, count in countt.items():
    print(char,count)
