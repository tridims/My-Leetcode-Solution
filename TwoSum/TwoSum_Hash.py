class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited_idx = {}

        for index, num in enumerate(nums):
            required_num = target - num

            if required_num in visited_idx:
                return [index, visited_idx[required_num]]
            else:
                visited_idx[num] = index

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))