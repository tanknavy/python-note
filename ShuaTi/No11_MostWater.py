def MostWater(inputList:list) ->int:
    res = 0
    for i in range(len(inputList)):
        for j in range(i+1,len(inputList)):
            res = max( (j-i) * min(inputList[i],inputList[j]), res)
    return res


inputList = [1,8,6,2,5,4,8,3,7]
print(MostWater(inputList))