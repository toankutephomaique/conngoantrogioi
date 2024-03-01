# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập một số nguyên dương n: "))

# Tính tổng các số chia hết cho 3 hoặc 5 từ 1 đến n
total = sum(i for i in range(1, n+1) if i % 3 == 0 or i % 5 == 0)

print("Tổng của các số chia hết cho 3 hoặc 5 từ 1 đến", n, "là:", total)