def kiem_tra_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên dương n: "))
print(f"Các số nguyên tố từ 2 đến {n} là:")
for i in range(2, n+1):
    if kiem_tra_nguyen_to(i):
        print(i, end=" ")