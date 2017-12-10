"""
Solution for http://adventofcode.com/2017/day/4

Run using: python day4.py
"""


INPUT_FILE = 'resources/day4-input.txt'


def is_valid_1(passphrase):
    """
    Returns True if the passphrase does not contain any duplicate words
    """
    tokens = sorted(passphrase.split())
    return not has_duplicate(tokens)


def is_valid_2(passphrase):
    """
    Returns True if the passphrase does not contain any words that are
    anagrams of each other
    """
    tokens = sorted(["".join(sorted(t)) for t in passphrase.split()])
    return not has_duplicate(tokens)


def has_duplicate(tokens):
    duplicate = next((
        token for i, token in enumerate(tokens)
        if i < len(tokens)-1 and tokens[i+1] == token
        ), None
    )
    return duplicate or None


with open(INPUT_FILE) as f:
    valid_1 = 0
    valid_2 = 0
    for line in f:
        if (is_valid_1(line)):
            valid_1 += 1
        if (is_valid_2(line)):
            valid_2 += 1
    print('Valid 1 count: {}'.format(valid_1))
    print('Valid 2 count: {}'.format(valid_2))
