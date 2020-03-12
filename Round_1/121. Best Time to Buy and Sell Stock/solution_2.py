class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        min_array = [min_price]

        # from left to right
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            min_array.append(min_price)

        print(min_array)

        # from right to left
        max_price = prices[-1]
        max_array = [max_price]
        for price in prices[-2::-1]:
            if price > max_price:
                max_price = price
            max_array.insert(0, max_price)

        print(max_array)

        profits = []
        for i, min_price in enumerate(min_array):
            delta = max_array[i] - min_price
            profits.append(delta)

        print(profits)

        return max(profits)

s = Solution()
s.maxProfit([7,1,5,3,6,4])


"""
Results:
Runtime: 168 ms, faster than 5.17% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14.1 MB, less than 17.24% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""