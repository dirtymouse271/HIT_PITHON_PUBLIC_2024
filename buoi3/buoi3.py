"""
"string la danh sach cac ky tu bat bien"
"cac cach khai bao string"
my_string = "hello"
my_string = 'hello'
my_string = '''hello'''
escape sequence
print('\a')
print('\t a')
print('ab\nc')
src = r'd:\coding\tennis'
print(src)
dinh dang chuoi
làm tròn số
s3 = "một phần ba: {0:.3f}".format(1/3)
print(s3)
định dạng số nguyên
s1 = "so "
can le
s4 = '|{:<10}|'.format('list')
print(s4)
#noi chuoi
s1 = "hit"
s2 = 'python'
s = s1+ s2
print(2)
xoa chuoi 
del s
s = 'hit'
s = s.upper()
print(s)
s = s.lower()
print(s)
s = 'hit python'
s = s.lower()
s1 = 'hit python'
s2 = 'hit python'
print(s == s1)
print(id(s1))
print(id(s2))
print("nhập chuỗi: ")
n = input()
countt = 0
for i in range(len(n)):
    if n[i] == n[0] and n[i] != ' ':
        countt+=1
    elif n[i] ==' ' and n[i+1] !=' ':
        countt+=1
print("số ký tự trong chuỗi là: ")
print(countt)
##list
l = [1,2,[3,4,5],6]
print(l[2][2])
l = [int(input()) for _ in range(10)]
print(l)
l = [[1,2,3],[4,5,6]]
l2 = [num for list in l for num in list if num % 2 == 0]
print(l2)
l = [1, 2, 3, 4, 5, 6]
l[2:] = [1, 2, 4, 5]#sửa
l[:0] = [8, 8, 8, 8]#chèn
l[0:] = []#xóa
l = [1, 2, 3, 4, 5, 6]
l1 = l.copy()#copy nội dung nhưng không copy địa chỉ 
print(id(l))
print(id(l1))
"""
print("nhập list số phần tử list a")
n = int(input())
print("nhập list a:")
a = [int(input()) for _ in range(n)]
# print("nhập list b")
# b = int([input()])
a.sort()
print(a)
