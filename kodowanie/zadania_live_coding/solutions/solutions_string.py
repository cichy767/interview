"""
Write a function:
def solutions(S, T)

that, given two strings S and T consisting of N and M characters, respectively, determines whether string T
can be obtained from string S by at most one simple operation from the set specified below.
The function should return a string:

* "INSERT c" if string T can be obtained from string S by inserting a single character "c" at the beginning of the string;
* "REMOVE c" if string T can be obtained from string S by deleting a single character "c" from the end of the string;
* "SWAP c d" if string T can be obtained from string S by swapping two adjacent characters "c" and "d" (these characters should be distinct and in the same order as in string S)
* "EQUAL" if no operations is needed (strings T and S are equal);
* "IMPOSSIBLE" if none of the above works.

Note that by characters "c" and "d" from the operations above, we mean any English alphabet lowercase letters.

For example:
given S = "gain" and T="again", the function should return "INSERT a";
given S = "parks" and T="park", the function should return "REMOVE s";
given S = "form" and T="from, the function should return "SWAP o r";
given S = "o" and T = "odd", the function should return "IMPOSSIBLE"
given S = "fift and T = fifth", the function should return "IMPOSSIBLE"

Assume that:
* N and M are integers within the range [1...100];
* strings S and T are made only of lowercase letters (a-z).
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

"""


def solutions(S, T):
    # Check for EQUAL
    if S == T:
        return "EQUAL"

    # Check for INSERT c
    if len(T) == len(S) + 1:
        if T[1:] == S:
            return f"INSERT {T[0]}"

    # Check for REMOVE c
    if len(S) == len(T) + 1:
        if S[:-1] == T:
            return f"REMOVE {S[-1]}"

    # Check for SWAP c d
    if len(S) == len(T):
        # Find the first index where characters differ
        diff = [i for i in range(len(S)) if S[i] != T[i]]
        print(diff)
        if len(diff) == 2 and S[diff[0]] == T[diff[1]] and S[diff[1]] == T[diff[0]] and diff[1] == diff[0] + 1:
            return f"SWAP {S[diff[0]]} {S[diff[1]]}"

    # If none of the above, return IMPOSSIBLE
    return "IMPOSSIBLE"


result = solutions('form', 'from')
print(result)