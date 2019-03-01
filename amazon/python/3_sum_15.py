def threeSum(nums):
    TARGET = 0
    nums.sort()
    length = len(nums)
    answer = []
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            # i += 1 cannot use this,
            # i is controlled by range, will cause forever loop
            continue
        left = i + 1
        right = length - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < TARGET:
                left += 1
            elif total > TARGET:
                right -= 1
            else:
                answer.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return answer


print(threeSum([-1, 0, 1, 2, -1, -4]))
