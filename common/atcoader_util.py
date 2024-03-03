from typing import List, Tuple
from collections import defaultdict
from itertools import combinations, permutations, product
import math
import itertools


def get_input():
    """標準入力を取得する"""
    return input()

def get_int_input():
    """整数の標準入力を取得する"""
    N = int(input())
    A = list(map(lambda x: int(x) - 1, input().split()))

def get_input_dict():
    N = int(input())
    from collections import Counter
    A = Counter(map(int, input().split()))

def max_bit_length(n):
    """最大ビット長を求める"""
    return n.bit_length()

def bit_count(n):
    """ビット数を求める"""
    return bin(n).count('1')

def bit_rol(n, bit, num_bit=64):
    """nのiビット目を取得する"""
    return ((n << (bit % num_bit)) % (1 << num_bit)) | (n >> (-bit % num_bit))

def bit_ror(n, bit, num_bit):
    return bit_rol(n, -bit, num_bit)

def gcd(a, b):
    """最大公約数を求める"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """最小公倍数を求める"""
    return a * b // gcd(a, b)

def combinations(n, r):
    """nCrを求める"""
    return math.comb(n, r)

def permutations(n, r):
    """nPrを求める"""
    return math.perm(n, r)

def is_prime(n):
    """素数判定"""
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    """エラトステネスの篩"""
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers

def get_divisors(n):
    """約数を求める"""
    i = 1
    divisors = []
    while i <= n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors

def get_divmod(a, b):
    """aをbで割った商と余りを求める"""
    return divmod(a, b)

def get_prime_factors(n):
    """素因数分解を求める"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def get_combinations(arr, r):
    """組み合わせを求める"""
    return list(itertools.combinations(arr, r))

def get_permutations(arr, r):
    """順列を求める"""
    return list(itertools.permutations(arr, r))

def factorial(n):
    """階乗を求める"""
    return math.factorial(n)

def binomial_coefficient(n, k):
    """二項係数を求める"""
    return math.comb(n, k)

def power_mod(x, y, p):
    """xのy乗をpで割った余りを求める"""
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def multiply_mod(a, b, mod):
    """aとbの積をmodで割った余りを求める"""
    return ((a % mod) * (b % mod)) % mod

def add_mod(a, b, mod):
    """aとbの和をmodで割った余りを求める"""
    return ((a % mod) + (b % mod)) % mod

def sub_mod(a, b, mod):
    """aとbの差をmodで割った余りを求める"""
    return ((a % mod) - (b % mod)) % mod

def divide_mod(a, b, mod):
    """aをbで割った余りをmodで割った余りを求める"""
    return multiply_mod(a, power_mod(b, mod - 2, mod), mod)

def get_fibonacci(n):
    """フィボナッチ数列を求める"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def bit_full_search(items):
    """ビット全探索"""
    n = len(items)
    # 2^nの全ての部分集合を列挙
    for i in range(2**n):
        subset = []
        for j in range(n):
            # j番目の要素が部分集合に含まれるかどうかをチェック
            if (i >> j) & 1:
                subset.append(items[j])
        yield subset

