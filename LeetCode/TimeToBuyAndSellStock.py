class Solution(object):
	def maxProfit(self, prices):
		minimum_price = float("inf")
		maximum_profit = 0

		for price in prices:
			minimum_price = min(minimum_price, price)
			maximum_profit = max(maximum_profit, price - minimum_price)

		return maximum_profit
