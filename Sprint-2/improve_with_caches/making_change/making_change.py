from typing import List


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values
    1, 2, 5, 10, 20, 50, 100, 200,
    return the number of ways to make the given total.

    Time Complexity: O(total × number_of_coins)
    Space Complexity: O(total × number_of_coins)
    """

    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    cache = {}

    return ways_to_make_change_helper(total, coins, cache)


def ways_to_make_change_helper(total: int, coins: List[int], cache: dict) -> int:
    """
    Helper function using manual memoisation.
    """

    key = (total, tuple(coins))

    if key in cache:
        return cache[key]

    if total == 0:
        return 1

    if total < 0 or not coins:
        return 0

    ways = 0
    coin = coins[0]

    max_count = total // coin

    for count in range(max_count + 1):
        remaining = total - (count * coin)
        ways += ways_to_make_change_helper(
            remaining,
            coins[1:],
            cache,
        )

    cache[key] = ways
    return ways