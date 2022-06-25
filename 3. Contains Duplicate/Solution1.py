class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        available = {}

        for num in nums:
            if num in available:
                return True
            available[num] = num
        return False

print(Solution().containsDuplicate([1,2,3,4]))