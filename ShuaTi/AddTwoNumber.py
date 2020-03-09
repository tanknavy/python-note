class LinkNode():
    def __init__(self,value):
        self.val = value
        self.next = None

class Solution():
    def addTwoNumber(self,l1,l2):
        res_dummyhead = LinkNode(0) # 空起点
        current  = res_dummyhead
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry,out = divmod(val1 + val2 + carry, 10) #除数和余数

            current.next = LinkNode(out)
            current = current.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return res_dummyhead.next

if __name__ == "__main__":
    Solution.addTwoNumber()
