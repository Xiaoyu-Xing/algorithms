def find_first_last_occurence(nums, x):
    first = find_first(nums, 0, len(nums) - 1, x)
    last = find_last(nums, 0, len(nums) - 1, x)
    return first, last


def find_first(nums, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        # If found x and (either reach the far left or the left num to the current num is smaller)
        if (mid == 0 or x > nums[mid - 1]) and nums[mid] == x:
            return mid
        # here it has to be moving the left pointer,
        elif x > nums[mid]:
            left = mid + 1
        # because right need to be moved, under either current num is larger or
        # there is left num that is equal to current num
        else:
            right = mid - 1
    return -1


def find_last(nums, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if (mid == len(nums) - 1 or x < nums[mid + 1]) and nums[mid] == x:
            return mid
        elif x < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


nums1 = [1, 1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
print(find_first_last_occurence(nums1, 9))


def find_first_recurrsive(nums, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == 0 or nums[mid - 1] < x) and nums[mid] == x:
            return mid
        elif nums[mid] < x:
            return find_first_recurrsive(nums, mid + 1, right, x)
        else:
            return find_first_recurrsive(nums, left, mid - 1, x)
    return -1


def find_last_recurrsive(nums, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == len(nums) - 1 or nums[mid + 1] > x) and nums[mid] == x:
            return mid
        elif x < nums[mid]:
            return find_last_recurrsive(nums, left, mid - 1, x)
        else:
            return find_last_recurrsive(nums, mid + 1, right, x)

    return -1


def find_first_last_occurence_recurssive(nums, x):
    first = find_first_recurrsive(nums, 0, len(nums) - 1, x)
    last = find_last_recurrsive(nums, 0, len(nums) - 1, x)
    return first, last


print(find_first_last_occurence_recurssive(nums1, 0))
