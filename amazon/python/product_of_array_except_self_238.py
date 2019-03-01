# Trick: every element in output = 
# product of all element in the left TIMES 
# product of all element in the right
# So two passes will solve the problem, 
# by accumulating the product from left and from right each pass
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplyer = 1
        output = []
        for i in range(len(nums)):
            output.append(multiplyer)
            multiplyer *= nums[i]
        multiplyer = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= multiplyer
            multiplyer *= nums[i]
        return output