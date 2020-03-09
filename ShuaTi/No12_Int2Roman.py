def Int2Roman(num:int) ->str:
    #int2r = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    #r2int = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    carry     = {1:"I",2:"X",3:"C",4:"M"}
    carryFive = {1:"V",2:"L",3:"D"}

    def rec(num,res):
        if num == 0:
            #with open("c:/tmp/roman.txt","w") as f: f.write(res)
            return res # this is the final result
        numlen = len(str(num))
        if num >= 10**(numlen-1) and (num <  4 * (10 **(numlen -1))):
            res += carry[numlen]
            num -= 10**(numlen-1)
        elif num >= 4 * (10 **(numlen -1)) and (num < 5 * (10 **(numlen-1))):
            res += carry[numlen] + carryFive[numlen]
            num -= 4 * (10 **(numlen -1))
        elif num >= 5 * (10 **(numlen-1)) and (num < 9 * (10 **(numlen-1))):
            res += carryFive[numlen]
            num -= 5 * (10 **(numlen -1))
        elif num >= 5 * (10 **(numlen-1)) and (num < 10 ** (numlen)):
            res += carry[numlen] + carry[numlen+1]
            num -= 9 * (10 ** (numlen - 1))
        else:
            raise Exception("wrong condition")
        rec(num,res)

    # 从上往下循环处理，上层处理结果传递到下层，最后一次性输出最终结果，可以改为递归
    # 如果本轮结果依赖于子处理过程，即必须先处理子问题才能得到父问题，如果不递归可能要使用stack
    def rec2(num,res):

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


# 如果使用递归，从上往下，上面结果依赖于本轮结果+子循环结果
    def rec3(num):
        #while num != 0: ""
        numlen = len(str(num))
        if num >= 10 ** (numlen - 1) and (num < 4 * (10 ** (numlen - 1))):
            res = carry[numlen]
            num -= 10 ** (numlen - 1)
            return res + rec3(num)
        elif num >= 4 * (10 ** (numlen - 1)) and (num < 5 * (10 ** (numlen - 1))):
            res = carry[numlen] + carryFive[numlen]
            num -= 4 * (10 ** (numlen - 1))
            return res + rec3(num)
        elif num >= 5 * (10 ** (numlen - 1)) and (num < 9 * (10 ** (numlen - 1))):
            res = carryFive[numlen]
            num -= 5 * (10 ** (numlen - 1))
            return res + rec3(num)
        elif num >= 5 * (10 ** (numlen - 1)) and (num < 10 ** (numlen)):
            res = carry[numlen] + carry[numlen + 1]
            num -= 9 * (10 ** (numlen - 1))
            return res + rec3(num)
        elif num == 0:
            return "" # 全部分解返回空字符，否则出错
        else:
            raise Exception("wrong condition")
        #return res

    res = ""
    #rec(num,res)
#    res = rec3(num,res);
    res = rec3(num);
    #with open("c:/tmp/roman.txt", "r") as f: res = f.read()
    return res


num = 1994
# 先查看具体使用了那个方法
print(Int2Roman(num)) # MCMXCIV
