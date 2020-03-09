def Int2Roman(num: int) -> str:
    carry = {1: "I", 2: "X", 3: "C", 4: "M"}
    carryFive = {1: "V", 2: "L", 3: "D"}
    res = ""
    while num != 0:
        numlen = len(str(num))
        if num >= 10 ** (numlen - 1) and (num < 4 * (10 ** (numlen - 1))):
            res += carry[numlen]
            num -= 10 ** (numlen - 1)
        elif num >= 4 * (10 ** (numlen - 1)) and (num < 5 * (10 ** (numlen - 1))):
            res += carry[numlen] + carryFive[numlen]
            num -= 4 * (10 ** (numlen - 1))
        elif num >= 5 * (10 ** (numlen - 1)) and (num < 9 * (10 ** (numlen - 1))):
            res += carryFive[numlen]
            num -= 5 * (10 ** (numlen - 1))
        elif num >= 5 * (10 ** (numlen - 1)) and (num < 10 ** (numlen)):
            res += carry[numlen] + carry[numlen + 1]
            num -= 9 * (10 ** (numlen - 1))
        else:
            raise Exception("wrong condition")
    return res

num = 1994
print(Int2Roman(num))
