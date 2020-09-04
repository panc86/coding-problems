# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
# Source: https://projecteuler.net/problem=3


def solution(N):
    i = 2
    while i * i < N:
        while N % i == 0:
            N /= i
        i += 1
    return N


# Run via the console
if __name__ == "__main__":
    import sys
    import time
    s = time.time()
    N = int(sys.argv[1])
    r = solution(N)
    e = time.time()
    print(f"Result: {list(r)}\ndone in {e - s:.10f} s")
