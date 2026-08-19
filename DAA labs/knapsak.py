def knapsack(price, wt, W):
    n = len(price)
    ratio = []
    for i in range(n):
        ratio.append((price[i] / wt[i], i))
    ratio.sort(reverse=True)
    profit = 0
    for r, i in ratio:
        if wt[i] <= W:
            profit += price[i]
            W -= wt[i]
        else:
            profit += price[i] * (W / wt[i])
            break
    return profit
price = (80, 40, 60)
wt = (20, 10, 30)
W = 50
print(knapsack(price, wt, W))
# Time Complexity: O(n log n)   Space Complexity: O(n)