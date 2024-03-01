def kiem_tra_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên dương n: "))

for i in range(n, 1, -1):
    if kiem_tra_nguyen_to(i):
        print(f"Số nguyên tố lớn nhất nhỏ hơn hoặc bằng {n} là: {i}")
        break