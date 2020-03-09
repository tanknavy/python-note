def str2int(inputString:str):
    trimed = inputString.lstrip()
    if trimed[0].isdigit() or trimed[0] == "-":
        if len(trimed) == 1:
            return 0 if str(trimed) == "-" else int(trimed)
        end =0
        for i in range(1,len(trimed)):
            if not trimed[i].isdigit():
                end =i
                break
        return trimed[0:end]
    return 0


#inputString = "   -4193 with words "
inputString = "   -3 www "
print(str2int(inputString))