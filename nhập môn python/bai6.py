# Hàm để tính giai thừa của một số nguyên dương
def tinh_giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)

# Nhập số nguyên dương từ người dùng
num = int(input("Nhập một số nguyên dương: "))

# Kiểm tra nếu số nhập vào là âm thì yêu cầu nhập lại
while num < 0:
    num = int(input("Vui lòng nhập một số nguyên dương: "))

# Tính và in ra giai thừa của số đó
if num == 0:
    print("Giai thừa của 0 là 1")
else:
    print("Giai thừa của", num, "là", tinh_giai_thua(num))