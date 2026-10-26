class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # x = 0
        # buy = 0
        # sell=-float("inf")
        # for i in prices:
        #     if i==0:
        #         buy = prices.index(i)
        #     x+=1
        # for j in range(buy,len(prices)):
        #     sell = max(sell,j)
        # pr = sell-buy
        # if pr>0:
        #     return pr
        # else:
        #     return 0
        buy = float("inf")
        sell=- float("inf")
        for i in prices:
            if i<buy:
                buy = min(i,buy)
            sell=max(sell,i-buy)
        return sell