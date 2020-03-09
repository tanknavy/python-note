def solution(num):
    num2str = str(num)
    num_len = len(str(num))
    i=0
    while(i < (num_len +1) // 2 ):
        if num2str[i] != num2str[num_len-i-1]:
            return False
        i += 1
    return True

inputInteger = -10
print(solution(inputInteger))