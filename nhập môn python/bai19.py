def tinh_luy_thua(num, so_chu_so):
    return num ** so_chu_so

def kiem_tra_armstrong(num):
    n = len(str(num))
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += tinh_luy_thua(digit, n)
        temp //= 10
    return total == num

n = int(input("Nhập số nguyên dương n: "))
print(f"Các số Armstrong từ 1 đến {n} là:")
for i in range(1, n+1):
    if kiem_tra_armstrong(i):
        print(i, end=" ")