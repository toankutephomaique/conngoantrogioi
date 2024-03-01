# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập một số nguyên dương n: "))

# Tính tổng các số lẻ từ 1 đến n
total = sum(i for i in range(1, n+1) if i % 2 != 0)

print("Tổng của các số lẻ từ 1 đến", n, "là:", total)