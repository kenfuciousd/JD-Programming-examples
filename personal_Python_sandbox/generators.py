#!/usr/bin/Python3
import sys
"""messing around with generators"""

def fibonacci(terms):
    i, a, b = 0, 0, 1
    while i < terms:
        i+=1
        #print(f"{a} and {b}")
        yield a
        a, b = b, a+b

fib = fibonacci(6)
for i in fib:
    print(i)

print("\n")

#
#a different use
mygenerator = (i for i in range(100) if i % 2 == 0)
for i in mygenerator:
    print(i)
print(list(mygenerator))
print(sys.getsizeof(mygenerator))

myList = [i for i in range(100) if i % 2 == 0]
#print(myList)
print(sys.getsizeof(myList))

