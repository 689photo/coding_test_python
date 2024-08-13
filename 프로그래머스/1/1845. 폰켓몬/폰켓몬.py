def solution(nums):
    num = len(nums) // 2
    ct = len(set(nums))
    
    if ct > num:
        return num
    else:
        return ct