# Hàm kiểm tra chuỗi đối xứng
def kiem_tra_chuoi_doi_xung(chuoi):
    chuoi = chuoi.lower()  # Chuyển đổi chuỗi thành chữ thường
    return chuoi == chuoi[::-1]  # So sánh chuỗi với chuỗi đảo ngược của nó

# Nhập chuỗi từ người dùng
chuoi = input("Nhập một chuỗi: ")

# Kiểm tra chuỗi có phải là chuỗi đối xứng hay không
if kiem_tra_chuoi_doi_xung(chuoi):
    print("Chuỗi đó là chuỗi đối xứng")
else:
    print("Chuỗi đó không phải là chuỗi đối xứng")