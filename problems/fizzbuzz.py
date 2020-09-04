# FizzBuzz game in python


def solution(N):
    for i in range(1, N):
        x = ""
        if i % 3 == 0:
            x += "Fizz"
        if i % 5 == 0:
            x += "Buzz"
        yield x or i


# Run via the console
if __name__ == "__main__":
    import sys
    import time
    s = time.time()
    N = int(sys.argv[1])
    r = solution(N)
    e = time.time()
    print(f"Result: {list(r)}\ndone in {e - s:.10f} s")
