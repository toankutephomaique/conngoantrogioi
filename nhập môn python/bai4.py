# Nhập ba số từ người dùng
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

# Tìm số lớn nhất trong ba số
max_num = max(num1, num2, num3)

# In ra số lớn nhất
print("Số lớn nhất trong ba số", num1, ",", num2, "và", num3, "là", max_num)