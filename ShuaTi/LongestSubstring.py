'''
Longest Substring w/o repeating characters
'''
def lengthOfSubstring(inputString):
    lenOfStr = len(inputString)
    max_len = 0
    res = ""
    for i in range(lenOfStr):
        for j in range(i,lenOfStr):
            if(allUnique(inputString,i,j)):
                max_len = max(j-i,max_len)
                if (j-i) > len(res): res = inputString[i:j]
                #res = inputString[i:j] if (len(res) < (j-i)) else res
    print("max_len: %d, res: %s" % (max_len,res))


def allUnique(inputString:str,start,end):
    charSet = set()
    for i in range(start,end):
        if inputString[i] in charSet:
            return False
        charSet.add(inputString[i])
    return True

def lengthOfSubstring2(inputString):
    lenOfStr = len(inputString)
    max_len =0
    res = ""
    i = 0
    charMap = {}
    for j in range(lenOfStr):
        if inputString[j] in charMap.keys():
            i = charMap.get(inputString[j]) + 1
        max_len = max(max_len, j-i+1)
        if (j-i+1) > len(res): res = inputString[i:j+1]
        charMap[inputString[j]] = j

    print("max_len: %d, res: %s" % (max_len, res))

input = "pwwkew"
lengthOfSubstring(input)
lengthOfSubstring2(input)


