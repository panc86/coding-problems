# Problem
# Find the smallest positive integer that does not occur in a given array A.

def solution(A):
    A.sort()
    min = 1
    for a in A:
        if a > min:
            return min
        if a > 0:
            min = a+1
    return min

# Method
# define the minimum value (1), iterate over A.
# Keep updating min until a is greated or the end of loop.
# Then return min

# Run via the console
if __name__ == "__main__":
    import sys
    import time
    s = time.time()
    A = [int(n) for n in sys.argv[1].split(",")]
    r = solution(A)
    e = time.time()
    print(f"Result: {r}\ndone in {e - s:.10f} s")
