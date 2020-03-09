class Solution():
    def convert(self,inputString,numRows):
        res = [[] for _ in range(numRows)]
        direction = -1
        row = 0
        for s in inputString:
            if row == 0 or row == numRows-1:
                direction = -direction
            res[row].append(s)
            row += direction

        result = "".join([e for r in res for e in r])
        return result

if __name__ == "__main__":
    inputString = "PAYPALISHIRING"
    print(Solution().convert(inputString,3))


