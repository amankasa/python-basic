def myFunc(n):
    return lambda a:a*n

doubler = myFunc(2)
tripler = myFunc(3)
four = myFunc(4)
print(doubler(10))
print(tripler(10))
print(four(10))