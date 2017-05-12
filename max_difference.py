# compute max difference of an array that contains list of stock prices
# for example
# list of price of stock A being [bought, sold, bought, sold] is [1,2,3,4]
# max difference for profit is 4 - 1 = 3


def max_difference(stock_prices):
    return max_sold(stock_prices) - min_bought(stock_prices)


def min_bought(odd_stock_prices):
    l = []

    for count, i in enumerate(odd_stock_prices):
        if count % 2 == 0:
            l.append(i)

    return min(l)


def max_sold(even_stock_prices):
    l = []

    for count, i in enumerate(even_stock_prices):
        if count % 2 == 1:
            l.append(i)

    return max(l)


print max_difference([1, 2, 3, 4])