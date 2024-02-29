def max_sum_positive_subsequence(nums):
    max_sum = float('-inf')  # Tổng lớn nhất của đoạn con có các số hạng dương liên tiếp
    current_sum = 0  # Tổng hiện tại của đoạn con có các số hạng dương liên tiếp
    max_subsequences = []  # Các đoạn con có tổng lớn nhất
    
    for i in range(len(nums)):
        num=nums[i]
        if num > 0:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
                max_subsequences = [[num]]
            elif current_sum == max_sum:
                max_subsequences[-1].append(num)
            # Reset current_sum if it becomes negative
            if current_sum < 0:
                current_sum = 0
        else:
            current_sum = 0
    
    return max_sum, max_subsequences

# Example usage:
mlist = [1, 2, 3, -1, 4, 5, 6, -2, -3, 7, 8, 9]
max_sum, subsequences = max_sum_positive_subsequence(mlist)
if subsequences:
    print("Tổng lớn nhất của đoạn con có các số hạng dương liên tiếp:", max_sum)
    print("Số đoạn con thoả mãn:", len(subsequences))
    print("Các đoạn con có tổng lớn nhất:")
    for subsequence in subsequences:
        print(subsequence)
else:
    print("Không có đoạn con nào có các số hạng dương liên tiếp trong danh sách.")