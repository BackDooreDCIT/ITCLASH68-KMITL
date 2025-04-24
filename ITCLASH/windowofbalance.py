def sliding_window_median(nums, k):
    medians = []
    
    for i in range(len(nums) - k + 1):
        window = sorted(nums[i:i + k])  # ใช้การ sort โดยไม่ใช้ library เสริม
        mid = k // 2
        
        if k % 2 == 1:
            medians.append(float(window[mid]))
        else:
            medians.append((window[mid - 1] + window[mid]) / 2)
    
    return " ".join(map(str, medians))

# รับ input
nums = list(map(int, input().split()))
k = int(input())

# ตรวจสอบผลลัพธ์
result = sliding_window_median(nums, k)
print(result)
