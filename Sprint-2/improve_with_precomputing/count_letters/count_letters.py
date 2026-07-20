def count_letters(s: str) -> int:
    """
    Count the number of letters that appear only in uppercase.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    uppercase = set()
    lowercase = set()

    for letter in s:
        if letter.isupper():
            uppercase.add(letter)
        elif letter.islower():
            lowercase.add(letter)

    count = 0

    for letter in uppercase:
        if letter.lower() not in lowercase:
            count += 1

    return count