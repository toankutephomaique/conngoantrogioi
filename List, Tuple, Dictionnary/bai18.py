# Nhập danh sách từ bàn phím
lst = [int(x) for x in input("Nhập danh sách các số: ").split()]

# Chèn danh sách [1, 2, 3] vào đầu danh sách
lst = [1, 2, 3] + lst

# Chèn danh sách [1, 2, 3] vào cuối danh sách
lst += [1, 2, 3]

# Chèn danh sách [1, 2, 3] vào vị trí thứ 5 của danh sách
lst = lst[:4] + [1, 2, 3] + lst[4:]

print("Danh sách sau khi chèn [1, 2, 3]:")
print(lst)