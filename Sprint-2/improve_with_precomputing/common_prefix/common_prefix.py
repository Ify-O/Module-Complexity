from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    Returns the longest string common at the start of any two strings.

    Time Complexity: O(n log n + n × m)
    Space Complexity: O(n)
    """

    if len(strings) < 2:
        return ""

    sorted_strings = sorted(strings)

    longest = ""

    for i in range(len(sorted_strings) - 1):
        common = find_common_prefix(
            sorted_strings[i],
            sorted_strings[i + 1],
        )

        if len(common) > len(longest):
            longest = common

    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))

    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]

    return left[:min_length]from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    Returns the longest string common at the start of any two strings.

    Time Complexity: O(n log n + n × m)
    Space Complexity: O(n)
    """

    if len(strings) < 2:
        return ""

    sorted_strings = sorted(strings)

    longest = ""

    for i in range(len(sorted_strings) - 1):
        common = find_common_prefix(
            sorted_strings[i],
            sorted_strings[i + 1],
        )

        if len(common) > len(longest):
            longest = common

    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))

    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]

    return left[:min_length]