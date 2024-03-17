def get_profit(prices, n_days, k_days):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, min(i + k_days + 1, n_days)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit


# n - количество дней прогноза
# k - срок годности рыбы
n, k = map(int, input().split())
forecast = list(map(int, input().split()))  # прогноз цены на рыбу по дням

result = get_profit(forecast, n, k)
print(result)
