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
            # print(f'current num = {n}, current tot = {tot}')

        # print(f"tot zero = {tot}")
        # print(f'num zero = {num_zero}')

        for i, n in enumerate(nums):
            if (num_zero == 1) and n != 0:
                nums[i] = 0
            elif (num_zero == 1) and n == 0:
                nums[i] = tot
            elif (num_zero > 1):
                nums[i] = 0
            else:
                nums[i] = int(tot / nums[i])
        
        return nums

print(Solution().productExceptSelf([0,4,0]))
