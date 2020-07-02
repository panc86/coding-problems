# Problem
# Return the value of the unpaired element in a given list.

def solution(A):
    result = 0
    for n in A:
        result ^= n
    return result

# Method
# XOR bitwise operator (^=) can detect overlapping values.

# Run via the console
if __name__ == "__main__":
    import sys
    import time
    s = time.time()
    A = [int(n) for n in sys.argv[1].split(",")]
    r = solution(A)
    e = time.time()
    print(f"Result: {r}\ndone in {e - s:.10f} s")
