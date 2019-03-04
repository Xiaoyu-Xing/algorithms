def find_pairs(nums1, nums2, target):
    nums1_set = set(nums1)
    ans = []
    for num in nums2:
        if target - num in nums1_set:
            ans.append([target - num, num])
    return ans


def find_pairs_index(nums1, nums2, target):
    nums1_dict = {}
    ans = []
    for i, num in enumerate(nums1):
        nums1_dict[num] = i
    for j, num in enumerate(nums2):
        if target - num in nums1_dict:
            ans.append([nums1_dict[target - num], j])
    return ans


arr1 = [1, 2, 3, 7, 5, 4]
arr2 = [0, 7, 4, 3, 2, 1]

x = 8
print(find_pairs_index(arr1, arr2, 8))
