# Problem
# Rotate an array to the right by a given number of steps.

def solution(A, K):
    asize = len(A)
    if asize == 0:
        return A
    K = K % asize
    return A[-K:] + A[:-K]

# Method
# 

# Run via the console
if __name__ == "__main__":
    import sys
    import time
    s = time.time()
    A, K = sys.argv[1].split(","), int(sys.argv[2])
    r = solution(A, K)
    e = time.time()
    print(f"Result: {r}\ndone in {e - s:.10f} s")
