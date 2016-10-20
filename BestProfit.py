"""
 Suppose we could access yesterday's stock prices as a list, where:

    The indices are the time in minutes past trade opening time, which was 9:30am local time.
    The values are the price in dollars of Apple stock at that time.

So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
"""



def solution(prices):
    """for every price, find the greatest number that follows and store the increase. if you find a higher increase, store that.

    Complexity:
    O(n^2)
    """
    profit = 0
    for index, price in enumerate(prices):
        _profit = max(prices[index:]) - price
        if _profit > profit:
            profit = _profit
    return profit



def solution(prices):
    """
    Best solution

    Largest increase between two consecutive numbers
    If we have a new high, calculate the profit from the low

    Complexity:
    O(n) time and O(1) space. We only loop through the list once.

    We'll greedily update min_price and max_profit, so we initialize
    them to the first price and the first possible profit.
    A greedy algorithm iterates through the problem space taking the
    optimal solution "so far," until it reaches the end.
    """

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for current_price in prices[1:]:
        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit




assert solution([10, 7, 5, 8, 11, 9, 2, 3]) == 6 # (buying for $5 and selling for $11)
assert solution([10, 7, 5, 3, -20]) == -2 # (the least we could have lost)