def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        d = 2
        while n % d != 0:
            d += 1
        if d == n:
            print('Простое')
        else:
            print('Составное')
        return n
    return wrapper

@is_prime
def sum_three(*args):
    a = sum(args)
    return a


result = sum_three(2, 3, 6)
print(result)