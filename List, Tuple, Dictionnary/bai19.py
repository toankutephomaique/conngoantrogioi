# Nhập danh sách từ bàn phím
lst = [int(x) for x in input("Nhập danh sách các số: ").split()]

# Nhập vị trí phần tử cần xóa từ bàn phím
k = int(input("Nhập vị trí phần tử cần xóa: "))

# Xác định vị trí thực sự trong danh sách
index = k - 1

# Kiểm tra xem vị trí cần xóa có hợp lệ hay không
if 0 <= index < len(lst):
    del lst[index]
    print("Danh sách sau khi xóa phần tử thứ", k, ":")
    print(lst)
else:
    print("Vị trí không hợp lệ!")