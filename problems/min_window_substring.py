# Problem
# Determine the smallest substring of N that contains all the characters in K. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.

# Examples

# Input: ["aaabaaddae", "aed"]
# Output: dae
# Input: ["aabdccdbcacd", "aad"]
# Output: aabd
# Input: ["ahffaksfajeeubsne", "jefaa"]
# Output: aksfaje
# Input: ["aaffhkksemckelloe", "fhea"]
# Output: affhkkse


from itertools import islice
from collections import deque, Counter


def iter_sliding_window(iterable, size):
    # slide a window over the iterable of size=size
    iterable = iter(iterable)
    window = deque(islice(iterable, size), maxlen=size)
    for item in iterable:
        yield tuple(window)
        window.append(item)
    if window:  
        # needed because if iterable was already empty before the `for`,
        # then the window would be yielded twice.
        yield tuple(window)


def solution(N, K):
    min_window_size = len(K)
    while min_window_size <= len(N):
        for window in iter_sliding_window(list(N), min_window_size):
            # count only chars of interest (K)
            tot = 0
            tmp_K = list(K)
            for char in window:
                if char in tmp_K:
                    tot += 1
                    tmp_K.pop(tmp_K.index(char))
                if tot == len(K):
                    return "".join(window)
        min_window_size += 1


# Run via the console
if __name__ == "__main__":
    import sys
    import time
    s = time.time()
    N, K = sys.argv[1].split(',')
    r = solution(N, K)
    e = time.time()
    print(f"Result: {r}\ndone in {e - s:.10f} s")
