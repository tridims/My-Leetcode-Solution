class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not (len(nums) == len(set(nums)))

print(Solution().containsDuplicate([1,2,3,4]))