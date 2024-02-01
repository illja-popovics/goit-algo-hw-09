import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount %= coin

    return result

def find_min_coins(amount):
    coins = [1, 2, 10, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    i = amount
    for coin in sorted(coins, reverse=True):
        count = i // coin
        if count > 0:
            result[coin] = count
            i %= coin

    return result




if __name__ == '__main__':
    amount = 113
    greedy_result = find_coins_greedy(amount)
    dynamic_result = find_min_coins(amount)

    print("Greedy Result:", greedy_result)
    print("Dynamic Result:", dynamic_result)



    start_time = time.time()
    find_coins_greedy(1000)  
    print("Greedy Algorithm --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    find_min_coins(1000)  
    print("Dynamic Programming --- %s seconds ---" % (time.time() - start_time))

