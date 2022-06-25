from typing import List

class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if (n == 0):
                curMax, curMin = 1, 1
                continue
        
            tmp = n * curMax
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax, curMax)

        return res

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

        