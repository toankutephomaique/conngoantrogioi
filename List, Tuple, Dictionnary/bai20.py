# Nhập danh sách từ bàn phím
lst = [int(x) for x in input("Nhập danh sách các số: ").split()]

# Sắp xếp danh sách theo thứ tự tăng dần
sorted_lst_ascending = sorted(lst)
print("Danh sách sau khi sắp xếp tăng dần:")
print(sorted_lst_ascending)

# Sắp xếp danh sách theo thứ tự giảm dần
sorted_lst_descending = sorted(lst, reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:")
print(sorted_lst_descending)