#Try to optimize by having it compute on demand in nextInt.
import random

#Global Initialization
N = 624
M = 397
A = 0x9908bd0df
UPPER = 0x80000000
LOWER = 0x7fffffff
m = [0 for i in range(N)]
mi = N

def setSeed(seed):
    global m, mi
    m[0] = seed & 0xffffff
    index = 1
    while (index < len(m)):
        m[index] = (69069 * m[index-1]) & 0xffffffff
        index = index + 1
    mi = 0

def nextInt():
    global m, mi, N, UPPER, LOWER, M, A
    if (mi >= N):
        mi = 0
    y = (m[mi] & UPPER) | (m[(mi+1) % N] & LOWER)
    m[mi] = m[(mi + M) % N] ^ (y >> 1)
    if (y % 2 != 0):
        m[mi] = m[mi] ^ A
    y = m[mi]
    mi = mi + 1
    y = y ^ (y >> 11)
    y = y  ^ ((y << 7) & 0x9d2c5680)
    y = y ^ (y >> 18)
    return y
