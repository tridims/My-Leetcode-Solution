class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_zero = 0
        tot = 1

        for n in nums:
            if n == 0:
                num_zero += 1
                continue
            tot *= n

        if (num_zero == 1):
            for i, n in enumerate(nums):
                if n != 0:
                    nums[i] = 0
                elif n == 0:
                    nums[i] = tot 

        elif (num_zero > 1):
            nums = [0 for _ in range(len(nums))]
        else:
            for i, n in enumerate(nums):
                nums[i] = int(tot / nums[i])
        
        return nums

print(Solution().productExceptSelf([0,4,0]))
print(Solution().productExceptSelf([1,5,2,3,8]))

