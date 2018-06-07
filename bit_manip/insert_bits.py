
# Given an integer n, replace its bits starting from the bit at position a to
# the bit at position b, inclusive, with the bits of integer k. Count from the
# least significant bit to the most significant bit, starting from 0.
def insert_bits(n, a, b, k):
    k = k << a
    mask = ((2**31)-1)
    mask = mask << (b+1)
    mask = mask  | ((2**a) -1)
    mask = mask  & ((2**31)-1)
    m = n & mask| k
    return m
