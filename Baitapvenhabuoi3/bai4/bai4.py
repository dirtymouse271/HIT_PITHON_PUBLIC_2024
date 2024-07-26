print("Nhập họ và tên: ")
full_name = input().strip()
normalized_name = ' '.join(word.capitalize() for word in full_name.split())
print("Chuỗi họ và tên đã được chuẩn hóa:", normalized_name)
