class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0] 
        difference = 0
        for i in range(len(prices)): 
            for j in range(i+1,len(prices)): 
                if prices[j] > prices[i]:
                    difference = prices[j]-prices[i] 
                    profit.append(difference) 
        return max(profit)        