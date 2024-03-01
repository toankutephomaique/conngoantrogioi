def tim_uoc(n):
    uoc = []
    for i in range(1, n):
        if n % i == 0:
            uoc.append(i)
    return uoc

def so_hoan_hao(n):
    so_hoan_hao_list = []
    for i in range(1, n+1):
        uoc = tim_uoc(i)
        if sum(uoc) == i:
            so_hoan_hao_list.append(i)
    return so_hoan_hao_list

n = int(input("Nhập số nguyên dương n: "))
so_hoan_hao_list = so_hoan_hao(n)

print(f"Các số hoàn hảo từ 1 đến {n} là: {so_hoan_hao_list}")