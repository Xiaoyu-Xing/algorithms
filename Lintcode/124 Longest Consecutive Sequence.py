class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, nums):
        if not nums:
            return 0
        count = {}
        for num in nums:
            count[num] = False
        print(count)
        max_length = 0
        for num in nums:
            if count[num]:
                continue
            count[num] = True
            curr_length = 1
            large = num + 1
            while large in count:
                count[large] = True
                curr_length += 1
                large += 1
            small = num - 1
            while small in count:
                count[small] = True
                curr_length += 1
                small -= 1
            # print(large, small, num, curr_length)
            max_length = max(max_length, curr_length)
        return max_length
