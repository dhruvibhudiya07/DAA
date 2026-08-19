#Time Complexity = O(n log n)....Space Complexity = O(n)
def knapsack(price, wt, W):
    n = len(price)
    ratio = []
    for i in range(n):
        ratio.append((price[i] / wt[i], price[i], wt[i], i))
    # Sort by price/weight ratio in descending order
    ratio.sort(key=lambda x: x[0], reverse=True)
    profit = 0
    items = []
    for r, pr, w, id in ratio:
        if w <= W:
            W -= w
            profit += pr
            items.append((id, 1))
        else:
            fraction = W / w
            profit += pr * fraction
            items.append((id, fraction))
            W = 0
            break
    return items, profit
price = (80, 40, 60)
wt = (15, 20, 10)
W = 100
print(knapsack(price, wt, W))