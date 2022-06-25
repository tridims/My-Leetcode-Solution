class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for _ in range(len(nums))]

        # compute prefix
        temp = 1
        for i in range(len(nums)):
            result[i] = temp
            temp *= nums[i]

        # compute result with postfix
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]
        
        return result


print(Solution().productExceptSelf([1,5,2,3,8]))
