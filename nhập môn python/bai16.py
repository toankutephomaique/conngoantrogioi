def tinh_tong_so_chan(danh_sach):
    tong = sum(x for x in danh_sach if x % 2 == 0)
    return tong

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tong_so_chan = tinh_tong_so_chan(danh_sach)

print("Tổng các số chẵn trong danh sách là:", tong_so_chan)