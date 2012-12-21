fib_table = {}
def fib(n):
    ret = fib_table.get(n, -1)
    if ret < 0:
        ret = fib_table[n] = fib_static(n)
    return ret
def fib_static(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
