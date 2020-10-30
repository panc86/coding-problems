# Problem
# There are N given points (o to N-1) on a plane. The K-th point is located at coordinates (X[K], Y[K]) and its tag is S[K]. We want to draw a circle centered on coordinates (0, 0). The circle should not contain two points with the same tag. What is the maximum number of points that can lie inside the circle?

# Write a function that, given a string S of length N and two arrays X, Y consisting of N integers each, returns the maxium number of points inside the circle. The circle may contain only points with distinct tags, and centered on coordinates (0, 0). Points that are on the border of the circle are included within it.

# Examples
# 1: Given S = 'ABDCA', X = [2, -1, -4, -3, 3], Y = [2, -2, 4, 1, -3], the function should return 3. There are three points that can be included in the circle: ('A', 2, 2), ('B', -1, -2), ('C', -3, 1). The next point ('A', 3, -3) has the same tag as ('A', 2, 2), so it cannot be included.

# 2: Given S = 'ABB', X = [1, -2, -2], Y = [1, -2, 2], the function should return 1. There are two points that cannot be included in the circle: ('B', -2, -2), ('B', -2, 2). They both have the tag 'B' and the same distance from coordinates (0, 0).

# 3: Given S = 'CCD', X = [1, -1, 2], Y = [1, -1, 2], the function should return 0. The points with tag 'C' have the same distance from coordinates (0, 0). (both C's exclude themselves leaving the circle without points)


# Solution
# 1. compute distances
# 2. find max hypotenuse `sqrt(a^2 + b^2)`
# 3. break collection when duplicate tag is found
# 4. remove outliers from result

import math

def hypotenuse(x, y):
    return math.sqrt(abs(x)**2 + abs(y)**2)


def remove_outliers(points, threshold):
    outliers = [t for t, r in points.items() if r > threshold]
    for outlier in outliers:
        del points[outlier]


def solution(S, X, Y):
    points = dict()

    for tag, x, y in zip(S, X, Y):
        h = hypotenuse(x, y)

        # stop if tag exists
        if tag in points:
            break

        # assign hypotenuse to tag
        points[tag] = h

    # remove anything further than h
    remove_outliers(points, h)

    # number of unique points in circle
    result = len(points)
    return result if result > 1 else 0
