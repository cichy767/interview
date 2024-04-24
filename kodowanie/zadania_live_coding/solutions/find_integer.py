"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(A):
    # Convert the list to a set to remove duplicates and enable faster lookup
    seen = set(A)

    # Start checking from the smallest positive integer, which is 1
    smallest_missing = 1

    # Keep incrementing until we find a missing number
    while smallest_missing in seen:
        smallest_missing += 1

    # Return the first missing positive integer
    return smallest_missing
