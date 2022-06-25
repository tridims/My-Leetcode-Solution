class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        max_profit = 0

        # print(prices)
        # data semua profit yang mungkin
        while (right < len(prices)):
            profit = prices[right] - prices[left]
            # print(f"dicek index {[left, right]}, profit = {profit}")

            if prices[right] < prices[left]:
                left = right

            if profit > max_profit:
                max_profit = profit
            
            right += 1

        return max_profit

a = Solution().maxProfit([2,1,4])
print(a)
        

