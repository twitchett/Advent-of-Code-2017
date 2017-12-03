"""
Solution to AoC 2017 day 1
https://adventofcode.com/2017/day/1
"""

import sys


def captcha(digits, step):
    # From the list of digits, create a new list of all the digits
    # that match the target digit, and sum them all together
    return sum([d for i, d in enumerate(digits) if d == digits[i - step]])


def run(digits):
    digits = [int(d) for d in [*digits]]   # Convert string to list of ints
    solution_1 = captcha(digits, 1)
    solution_2 = captcha(digits, len(digits) // 2)
    print("Your solution is: {} (part 1), {} (part 2)".format(solution_1, solution_2))


if len(sys.argv) != 2:
    raise Exception("Syntax: python day1.py [input]")
else:
    run(sys.argv[1])
