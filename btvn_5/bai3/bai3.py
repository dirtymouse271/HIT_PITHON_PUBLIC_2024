import random
password_list = ["CNTT", "KHMT", "KTPM", "HTTT"]
N = 10
accounts = {}
for i in range(N):
    maSinhVien = f"202360{str(i+1).zfill(4)}"
    tenTaiKhoan = f"Account{i+1}"
    matKhau = random.choice(password_list)
    password =matKhau+maSinhVien
    accounts[tenTaiKhoan] = {
        "Username": maSinhVien,
        "Password": password
    }
print(accounts)

