def longRepeatSubString(inputString:str):
    length = len(inputString)
    max_len = 0
    res = ""
    charMap = {}
    for j in range(length):
        if input[j] in charMap:
            pos = charMap.get(input[j])
            max_len = max(len(res), j-pos+1)
            res = input[pos:j+1] if (j-pos+1) > len(res) else res
        charMap[input[j]] = j
    print("max_len: %d, res: %s" % (max_len, res))


input = "babadefghd"
ss = longRepeatSubString(input)