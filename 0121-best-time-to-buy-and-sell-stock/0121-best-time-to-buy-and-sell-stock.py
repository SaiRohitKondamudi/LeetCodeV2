class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxprofit = 0
        
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                maxprofit = max(maxprofit, prices[right] - prices[left])
            right += 1

        return maxprofit