"""
Solution for https://adventofcode.com/2017/day/3
Run using: python day3.py [input]
"""

import sys

# Offsets used to calculate the distance from the origin
# for points lying along the axes
AXES = {
    'E': 1,
    'N': 3,
    'W': 5,
    'S': 7
}


def calculate_length_size(n):
    """
    Returns the number of elements on each side of a ring at position n
    """
    return (2 * n) - 1


def calculate_axis_point(n, axis):
    """
    Gets the value of the element directly north, south, east or west
    of the origin by n spaces (i.e. along the axes)
    """
    offset = AXES[axis]
    return 1 + sum([((i - 1) * 8) + offset for i in range(1, n)])


def calculate_upper_bound(n):
    """
    Calculates the maximum value of a grid of size n
    """
    length_size = calculate_length_size(n)
    upper = calculate_axis_point(n, 'S') + (length_size - 1)/2
    return int(upper)


def calculate_nearest_axis(target, points):
    """
    Finds the nearest axis point and returns the absolute
    distance to it from the target
    """
    dist = None
    for axis, p in points:
        if not dist or abs(p - target) < dist:
            dist = abs(p - target)
    return dist


def main(target):
    # n = size of grid, i.e. the length of one side
    size = 1
    bound = calculate_upper_bound(size)
    while bound < target:
        size += 1
        bound = calculate_upper_bound(size)
    print('Found grid size: {}'.format(size))

    axis_points = [(axis, calculate_axis_point(size, axis)) for axis in AXES.keys()]
    print('Found axis points:', axis_points)

    axis_dist = calculate_nearest_axis(target, axis_points)
    print('Found distance from axis point: {}'.format(axis_dist))

    total_dist = (size - 1) + axis_dist
    print('Manhattan distance for input {}: {}'.format(target, total_dist))


if len(sys.argv) != 2:
    raise Exception("Syntax: python day3.py [input]")
else:
    main(int(sys.argv[1]))
