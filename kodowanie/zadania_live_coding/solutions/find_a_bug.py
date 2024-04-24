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
    print(f"A: {A} X: {X}")
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        print(f"start loop l: {l} r: {r}")
        m = (l + r) // 2
        print(f"m: {m}")
        if A[m] > X:
            r = m - 1
            print(f"reducing r! X: {X} A[m]: {A[m]} r: {r}")
        else:
            l = m
            print(f"X: {X} A[m]: {A[m]} l: {l}")

    if A[l] == X:
        print(f"A[l]: {A[l]} X: {X}")
        return l
    return -1


res = solution([1, 2, 3], 2)
print(f"res: {res}")

# def solution(A, X):
#     N = len(A)
#     if N == 0:
#         return -1
#     l = 0
#     r = N - 1
#     while l < r:  # Change 1: Modify the loop condition to allow 'l' to equal 'r'
#         m = (l + r) // 2
#         if A[m] < X:
#             l = m + 1  # Change 2: Ensure 'l' progresses past 'm'
#         elif A[m] > X:
#             r = m - 1
#         else:
#             return m  # Found X, return the index
#
#     return -1  # X was not found in the array
