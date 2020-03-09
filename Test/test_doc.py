'''
test fixture,test case,test suite, test runner
doctest搜索看起来像交互python session的文本，并执行会话
'''
import math
def cal(n:int):
    """
    get a number ** 2
    :param n:
    :return: n**2

    Examples:
    >>> ll = [1,2,3]
    >>> ll
    [1, 2, 3]
    >>> cal(2)
    4
    >>> cal(4)
    16
    """
    #tmp = str(n)
    if isinstance(n,int):
        return int(math.pow(n,2))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    #doctest.testmod()
    #doctest.testfile()
    #doctest.testsource()
    # python examply.py -v # 命令行时终端

