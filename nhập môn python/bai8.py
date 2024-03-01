# Hàm để tính số Fibonacci tại vị trí n
def fibonacci(n):
    if n <= 0:
        return "Vị trí phải là một số nguyên dương"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Nhập vị trí trong dãy Fibonacci từ người dùng
n = int(input("Nhập vị trí trong dãy Fibonacci: "))

# In ra số Fibonacci tại vị trí n
result = fibonacci(n)
if type(result) == str:
    print(result)
else:
    print(f"Số Fibonacci tại vị trí {n} là {result}")