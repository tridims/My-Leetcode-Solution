from typing import List

class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 0, 0

        for n in nums:
            tmp = n + curMax
            curMax = max(tmp, n + curMin, n)
            curMin = min(tmp, n + curMin, n)
            res = max(res, curMax, curMax)

        return res

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([5,4,-1,7,8]))


        