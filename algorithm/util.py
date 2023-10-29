import numpy
import itertools
import math

int_list = [int(i) for i in input().split(',')]
int_list = map()
# intリストを文字列に結合
"".join([str(_) for _ in int_list])

# int配列に変換
int_list = [int(_) for _ in str_list]

# 16進数
l_i = [0, 64, 128, 192, 256]
l_i_hex1 = [hex(i) for i in l_i]


arr = []
for i in range(3):
  arr.append([int(_) for _ in input().split()])
arr = numpy.array(arr)

# 組み合わせ
def _permutations(list):
    if len(list) == 1:
        return [list]
    else:
        result = [] 
        for i, val in enumerate(list):
            rest = _permutations(list[:i] + list[i+1:])
            for rest_perm in rest:
                perm = [val] + rest_perm
                result.append(perm)
        return result

# nCr組み合わせ
def cmb_1():
    nCr = {}
    def cmb(n, r):
        if r == 0 or r == n: return 1
        if r == 1: return n
        if (n,r) in nCr: return nCr[(n,r)]
        nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
        return nCr[(n,r)]
    a = cmb(n,r)

def cmb_2():
    from operator import mul
    from functools import reduce
    def cmb(n,r):
        r = min(n-r,r)
        if r == 0: return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1,r + 1))
        return over // under
    a = cmb(n, r)
    
def cmb_3():
    from scipy.special import comb
    a = comb(n, r, exact=True)  

#重複あり、順列（何回同じのを選んでもいい、順番で区別する）
itertools.product('調べる文字列', repeat=選ぶ回数)

#重複なし、順列（同じのは1回しか選べない、順番で区別する）
itertools.permutations('調べる文字列',選ぶ回数)

#重複あり、組み合わせ（何回同じのを選んでもいい、順番では区別しない）
itertools.combinations_with_replacement('調べる文字列',選ぶ回数)

#重複なし、組み合わせ（同じのは1回しか選べない、順番では区別しない）
itertools.combinations('調べる文字列',選ぶ回数)

#最大公約数
print(math.gcd(27, 18, 9, 3))
#最小公倍数
print(math.lcm(27, 18, 9, 3))