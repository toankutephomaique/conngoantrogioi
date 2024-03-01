# Nhập tên và năm sinh từ người dùng
name = input("Nhập tên của bạn: ")
year_of_birth = int(input("Nhập năm sinh của bạn: "))

# Tính tuổi của bạn
current_year = 2022
age = current_year - year_of_birth

# In ra chuỗi chứa tên và tuổi của bạn
print("Xin chào,", name + "! Bạn", age, "tuổi.")