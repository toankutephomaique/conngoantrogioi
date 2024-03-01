def chuyen_phan_tu_duong_len_dau(danh_sach):
    phan_tu_duong = [x for x in danh_sach if x > 0]
    phan_tu_am = [x for x in danh_sach if x <= 0]
    
    return phan_tu_duong + phan_tu_am

danh_sach = [2, -3, 4, 7, -1, 8, 10, -5, 6]
danh_sach_sau_khi_chuyen = chuyen_phan_tu_duong_len_dau(danh_sach)

print("Danh sách sau khi chuyển các phần tử dương lên đầu:")
print(danh_sach_sau_khi_chuyen)