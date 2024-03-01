# Nhập giá trị của hai biến từ người dùng
a = input("Nhập giá trị biến a: ")
b = input("Nhập giá trị biến b: ")

# In ra giá trị của hai biến trước khi đổi chỗ
print("Giá trị của biến a trước khi đổi chỗ:", a)
print("Giá trị của biến b trước khi đổi chỗ:", b)

# Đổi chỗ giá trị của hai biến
a, b = b, a

# In ra giá trị của hai biến sau khi đổi chỗ
print("Giá trị của biến a sau khi đổi chỗ:", a)
print("Giá trị của biến b sau khi đổi chỗ:", b)