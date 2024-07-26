N = int(input("Nhập số lượng số nguyên: "))
number = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
so_cuoi_thay_thich = {1, 3, 5, 7, 9}
so_thay_thich = [num for num in number if num %10 in so_cuoi_thay_thich]
so_thay_thich.sort()
print(len(so_thay_thich))
print(so_thay_thich)
