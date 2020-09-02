# Problem
# Return the length of the longest binary gap of a positive integer.
# A binary gap within a positive integer N is any maximal sequence of
# consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

def solution(N):
    return len(max(format(N, 'b').strip('0').split('1')))

# Method
# after converting the integer into binary format, strip zeros and split by ones.
# then find the length of the largest item.

# Run via the console
if __name__ == "__main__":
    import sys
    import time
    s = time.time()
    N = int(sys.argv[1])
    r = solution(N)
    e = time.time()
    print(f"Result: {r}\ndone in {e - s:.10f} s")
