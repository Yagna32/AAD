def coinChange(coins,amount):
    dp = [float('inf')]* (amount+1)
    dp[0] = 0
    coin_used = [[] for _ in range(amount+1)]
    for coin in coins:
        for i in range(coin,amount+1):
            if dp[i] > (dp[i-coin]+1):
                dp[i] = dp[i-coin] + 1
                coin_used[i] = coin_used[i-coin] + [coin]
    if dp[amount] == float('inf'):
        return -1,[]
    else :
        return dp[amount], coin_used[amount]

coins = [4,6,1]
amount = 8
min_coins, coins_used = coinChange(coins,amount)
print('Minimum amount of coins needed :',min_coins)
print('Coins used : ',coins_used)
