def coin_sum(coins, change):
    coins.sort(reverse=True)
    coins_to_change = {}
    total_coins = 0

    for coin in coins:
        if change >= coin:
            count = change // coin
            coins_to_change[coin] = count
            total_coins += count
            change -= coin * count

    if change != 0:
        print("Error")
        return

    print(f"Number of coins to take: {total_coins}")
    for coin, count in coins_to_change.items():
        print(f"{count} coin(s) with value {coin}")



coins_line = [int(x) for x in input().split(", ")]
searched_change = int(input())
coin_sum(coins_line, searched_change)