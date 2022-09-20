class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=[]
        for i in range(len(prices)-1):
            if max(prices[i+1:])>prices[i]:
                a=max(prices[i+1:])
                max_profit.append(a-prices[i])
                
        if max_profit:
            return max(max_profit)
        else:
            return 0
