from typing import List

class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        res = max(nums)

        for n in nums:
            if sum + n < 0:
                sum = 0
            else:
                sum += n
            res = sum if sum > res and sum != 0 else res
        
        return res

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([5,4,-1,7,8]))

            