print("Nhập chuỗi s1: ")
s1 = str(input())
print("Nhập chuỗi s2: ")
s2 = str(input())
s1_reverse = s1[::-1]
print(s1_reverse)
print("Nhập a: ")
while True:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    
    # Kiểm tra điều kiện
    if 1 <= a < b <= len(s2):
        break
    else:
        print("Hai số nguyên a và b phải thỏa mãn điều kiện 1 <= a < b <= len(s2). Vui lòng nhập lại.")
a -= 1
b -= 1
s2_reversed_part = s2[a:b+1][::-1]
s2_result = s2[:a] + s2_reversed_part + s2[b+1:]
print(s2_result)
s3 = s1[1::2]
print("Chuỗi s3 sau khi xóa các kí tự vị trí chẵn từ s1 là:", s3)
s4 = ''.join([i + j for i, j in zip(s1, s2)])
s4 += s1[len(s2):] + s2[len(s1):]
print("Chuỗi s4 sau khi đan xen các kí tự của s1 và s2 là:", s4)
new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]
print("Chuỗi mới của s1 sau khi đổi chỗ: ", new_s1)
print("Chuỗi mới của s2 sau khi đổi chỗ: ", new_s2)


