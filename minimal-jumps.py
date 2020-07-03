# Problem
# Count the minimal number of jumps one must perform from X to Y, given a jump fixed distance D.

def solution(X, Y, D):
    # write your code in Python 3.6
    distance = Y - X
    if distance % D == 0:
        return distance // D
    else:
        return distance // D + 1

# Method
# Cumpute the total distance then return the ratio between
# the distance and the step if that ratio has no reminder,
# otherwise return the distance and the step + 1 (to account for the removed reminder)

# Run via the console
if __name__ == "__main__":
    import sys
    import time
    s = time.time()
    X, Y, D = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    r = solution(X, Y, D)
    e = time.time()
    print(f"Result: {r}\ndone in {e - s:.10f} s")
