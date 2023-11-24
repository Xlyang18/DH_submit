def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def factorize_integer(n):
    factors = prime_factors(n)
    if len(factors) == 0:
        return f"{n} is a prime number."
    else:
        factorization = f"{n} = " + " * ".join(map(str, factors))
        return factorization

# 输入正整数
n = int(input("请输入一个正整数："))

if n <= 0:
    print("请输入一个正整数。")
else:
    result = factorize_integer(n)
    print(result)
