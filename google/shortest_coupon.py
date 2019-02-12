def shortes_coupon(s: 'list') ->'int':
    ret = len(s) + 1
    count = {}
    for i, number in enumerate(s):
        if number in count:
            ret = min(ret, i - count[number] + 1)
        count[number] = i
    if ret == len(s) + 1:
        return -1
    return ret


print(shortes_coupon([5, 3, 4, 2, 3, 4, 5, 7]))
print(shortes_coupon([]))
print(shortes_coupon([1, 2, 3, 4, 5, 6, 7]))
print(shortes_coupon([1, 2, 3, 4, 5, 6, 7, 1]))
print(shortes_coupon([1, 1, 3, 4, 5, 1, 7, 1]))
print(shortes_coupon([1, 2, 3, 4, 5, 1, 7, 1]))
print(shortes_coupon([1, 2, 3, 1, 5, 1, 7, 1, 2, 1, 1, 5, 1, 7, 1]))
