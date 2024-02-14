class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        
        for i in range(len(prices)):
            if i == 0: price = prices[i]
            elif prices[i] < price: price = prices[i]
            elif prices[i] - price > ans: ans = prices[i] - price

        return ans