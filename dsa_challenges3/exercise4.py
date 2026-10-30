def minimum_coins(coins, amount):
    # Initialize a DP table with an impossible maximum value (amount + 1)
    # dp[i] will store the minimum coins needed for amount i
    dp = [amount + 1] * (amount + 1)
    
    # Base case: 0 coins are needed to make an amount of 0
    dp[0] = 0
    
    # Calculate the minimum coins needed for every sub-amount from 1 up to amount
    for i in range(1, amount + 1):
        for coin in coins:
            # Check if the coin can be part of the solution
            if i - coin >= 0:
                # Core logic: Can we reach this amount using fewer coins?
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    # If dp[amount] didn't change, it means the amount cannot be formed
    return dp[amount] if dp[amount] != amount + 1 else -1
