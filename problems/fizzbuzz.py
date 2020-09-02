# FizzBuzz game in python

N = 50

for i in range(1, N):
    x = ""
    if i % 3 == 0:
        x += "Fizz"
    if i % 5 == 0:
        x += "Buzz"
    print(x or i)
