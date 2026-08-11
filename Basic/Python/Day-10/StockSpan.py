prices = [10,21,30,12,8,10]

def stock_span(prices):
    result = []
    stack = []

    for price in prices:
        span = 1
        while stack and stack[-1][0]<=price:
            previous_price,previous_span = stack.pop()
            span += previous_span

        stack.append((price,span))

        result.append(span)

    return result

res = stock_span(prices)
print(res)