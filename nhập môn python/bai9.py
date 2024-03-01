# Nhập danh sách các số nguyên từ người dùng
nums = input("Nhập danh sách các số nguyên, cách nhau bởi dấu cách: ").split()
nums = [int(num) for num in nums]

# Kiểm tra nếu danh sách có ít hơn hai số
if len(nums) < 2:
    print("Danh sách phải chứa ít nhất hai số")
else:
    # Sắp xếp danh sách theo thứ tự giảm dần
    sorted_nums = sorted(nums, reverse=True)
    
    # Loại bỏ các số trùng lặp
    unique_nums = list(set(sorted_nums))
    
    # Kiểm tra nếu danh sách chỉ chứa các số trùng lặp
    if len(unique_nums) == 1:
        print("Danh sách chỉ chứa các số trùng lặp")
    else:
        second_largest = unique_nums[1]
        print("Số lớn thứ hai trong danh sách là:", second_largest)