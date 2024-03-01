# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Nhập số từ người dùng
num = int(input("Nhập một số nguyên dương: "))

# Kiểm tra số nhập vào có phải là số nguyên tố hay không
if kiem_tra_so_nguyen_to(num):
    print(num, "là số nguyên tố")
else:
    print(num, "không phải là số nguyên tố")