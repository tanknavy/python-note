
def reverse(inputInteger):
    neg = inputInteger < 0

    mod = abs(inputInteger)
    res =0
    while mod != 0:
       res = res * 10 + mod  % 10
       mod = mod // 10

    if res  > 2**32 -1:
        return 0
    return -res if neg else res

print(reverse(-123))
