class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = prices[0]
        for i in range(1,len(prices)):

            minPrice = min(minPrice, prices[i])
            maxProf = max(maxProf, prices[i]-minPrice)
        return maxProf











