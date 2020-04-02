class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_num = len(prices)

        if total_num == 0 or total_num == 1:
            return 0

        # change to generator since the memory usage is high
        positive_deltas = (prices[i] - prices[i - 1] for i in range(1, total_num) if prices[i] - prices[i - 1] > 0)

        return sum(positive_deltas)
