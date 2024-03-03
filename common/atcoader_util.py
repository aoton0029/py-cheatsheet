from typing import List, Tuple
from collections import defaultdict
from itertools import combinations, permutations, product
import math
import itertools


class AtCoderUtil:

	@staticmethod
	def gcd(a, b):
		while b:
			a, b = b, a % b
		return a

	@staticmethod
	def lcm(a, b):
		return a * b // AtCoderUtil.gcd(a, b)

	@staticmethod
	def combinations(n, r):
		return math.comb(n, r)

	@staticmethod
	def permutations(n, r):
		return math.perm(n, r)

	@staticmethod
	def is_prime(n):
		if n == 1: return False
		for k in range(2, int(math.sqrt(n)) + 1):
			if n % k == 0:
				return False
		return True

	@staticmethod
	def sieve_of_eratosthenes(n):
		primes = [True for i in range(n+1)]
		p = 2
		while (p * p <= n):
			if (primes[p] == True):
				for i in range(p * p, n+1, p):
					primes[i] = False
			p += 1
		prime_numbers = [p for p in range(2, n) if primes[p]]
		return prime_numbers

	@staticmethod
	def get_divisors(n):
		i = 1
		divisors = []
		while i <= n:
			if n % i == 0:
				divisors.append(i)
			i += 1
		return divisors

	@staticmethod
	def get_prime_factors(n):
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

	@staticmethod
	def get_combinations(arr, r):
		return list(itertools.combinations(arr, r))

	@staticmethod
	def get_permutations(arr, r):
		return list(itertools.permutations(arr, r))

	@staticmethod
	def factorial(n):
		return math.factorial(n)

	@staticmethod
	def binomial_coefficient(n, k):
		return math.comb(n, k)

	@staticmethod
	def power_mod(x, y, p):
		res = 1
		x = x % p
		while y > 0:
			if y & 1:
				res = (res * x) % p
			y = y >> 1
			x = (x * x) % p
		return res

	@staticmethod
	def multiply_mod(a, b, mod):
		return ((a % mod) * (b % mod)) % mod

	@staticmethod
	def add_mod(a, b, mod):
		return ((a % mod) + (b % mod)) % mod

	@staticmethod
	def subtract_mod(a, b, mod):
		return ((a % mod) - (b % mod)) % mod

	@staticmethod
	def divide_mod(a, b, mod):
		return AtCoderUtil.multiply_mod(a, AtCoderUtil.power_mod(b, mod - 2, mod), mod)

	@staticmethod
	def get_fibonacci(n):
		if n <= 0:
			return 0
		elif n == 1:
			return 1
		else:
			a, b = 0, 1
			for _ in range(n - 1):
				a, b = b, a + b
			return b

	@staticmethod
	def get_combinations(iterable, r):
		return list(itertools.combinations(iterable, r))

	@staticmethod
	def get_combinations_with_replacement(iterable, r):
		return list(itertools.combinations_with_replacement(iterable, r))

	@staticmethod
	def get_permutations(iterable, r):
		return list(itertools.permutations(iterable, r))

	@staticmethod
	def get_cartesian_product(*iterables, repeat=1):
		return list(itertools.product(*iterables, repeat=repeat))

	@staticmethod
	def get_power_set(iterable):
		s = list(iterable)
		return list(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1)))

	@staticmethod
	def get_cyclic_permutations(iterable):
		return list(itertools.permutations(iterable, len(iterable)))

	@staticmethod
	def get_group_by(iterable, key_func=None):
		return list(itertools.groupby(sorted(iterable, key=key_func), key_func))

	@staticmethod
	def get_all_true(iterable, pred=None):
		return list(itertools.filterfalse(pred, iterable))

	@staticmethod
	def get_accumulate(iterable, func=None):
		return list(itertools.accumulate(iterable, func))

	@staticmethod
	def get_chain(*iterables):
		return list(itertools.chain(*iterables))

	@staticmethod
	def get_slice(iterable, start, stop):
		return list(itertools.islice(iterable, start, stop))

	@staticmethod
	def get_repeat(elem, times=None):
		return list(itertools.repeat(elem, times))

	@staticmethod
	def get_starmap(func, iterable):
		return list(itertools.starmap(func, iterable))

	@staticmethod
	def get_takewhile(pred, iterable):
		return list(itertools.takewhile(pred, iterable))

	@staticmethod
	def get_zip_longest(*iterables, fillvalue=None):
		return list(itertools.zip_longest(*iterables, fillvalue=fillvalue))

	@staticmethod
	def get_count(start=0, step=1):
		return itertools.count(start, step)

	@staticmethod
	def get_cycle(iterable):
		return itertools.cycle(iterable)

	@staticmethod
	def get_dropwhile(pred, iterable):
		return list(itertools.dropwhile(pred, iterable))

	@staticmethod
	def get_tee(iterable, n=2):
		return itertools.tee(iterable, n)
	
