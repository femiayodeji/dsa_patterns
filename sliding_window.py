class BestBuy:
    def brute(prices = [7, 1, 5, 3, 6, 4]):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        return max_profit

    def optimal(prices = [7, 1, 5, 3, 6, 4]):
        max_profit = 0
        min_price = float('inf')
        for right in range(len(prices)):
            if prices[right] < min_price:
                min_price = prices[right]
            else:
                max_profit = max(prices[right]-min_price, max_profit)
        return max_profit
