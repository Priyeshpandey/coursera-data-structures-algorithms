# Uses python3
import sys


def binary_search(a, x):
    """Binary Search.

    Implementation of binary search algorithm.
    Returns the index if the element is found in the array, -1 otherwise.

    Samples:
    >>> n = 5; a = [1, 5, 8, 12, 13]
    >>> binary_search(a, 8)
    2
    >>> binary_search(a, 1)
    0
    >>> binary_search(a, 23)
    -1
    >>> binary_search(a, 1)
    0
    >>> binary_search(a, 11)
    -1
    """
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2

        a_mid = a[mid]
        if x == a_mid:
            return mid

        # left--mid--x--right
        if a_mid < x:
            left = mid + 1

        # left--x--mid--right
        elif x < a_mid:
            right = mid - 1

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end=" ")
        print(binary_search(a, x), end=" ")
