# array, hash map
def two_sum(array, target):
    nums = {}
    for i, num in enumerate(array):
        if target - num in nums:
            return [nums[target - num], i]
        nums[num] = i


answer = two_sum([2, 11, 7, 15], 9)
print(answer)

# Note: Use hashmap when memorizing something would help.
