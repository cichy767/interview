"""
You are given an implementation of a function:

def solution(A, X)

This function, when giving an array A of N integers, sorted in non-decreasing order, and some integer X, looks for X in A.
If X is present in A, then the function returns position of (some) occurrence of X in A.
Otherwise the function returns -1.

For example given the following array:
A[0] = 1
A[1] = 2
A[2] = 5
A[3] = 9
A[4] = 9

and X = 5, the function should return 2, as A[2] = 5

The attached code is still incorrect for some inputs.
Despite the errors(s), the code may produce a correct answer for the example test cases.
The goal of this exercise is to find and fix the bug(s) in the implementation.
You can modify at most three lines.

Assume that:
* N is an integer within the range [0...100000];
* each element of Array A is an integer within the range [-2000000000...2000000000];
* array A is sorted in non-decreasing order;
* X is an integer within the range [-2000000000...2000000000]



"""


def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        # Górny środek gwarantuje postęp także wtedy, gdy r == l + 1.
        m = (l + r + 1) // 2
        if A[m] > X:
            r = m - 1
        else:
            l = m

    if A[l] == X:
        return l
    return -1


if __name__ == "__main__":
    print(solution([1, 2, 3], 2))
