'''
自平衡二叉树
'''
import math
import random


class my_queue: # 自定义一个FIFO队列
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        return self.head == self.tail

    def push(self):
        self.data.append(data)
        sefl.tail = self.tail + 1

    def pop(self):
        ret = self.data[head]
        self.head = self.head + 1

    def count(self):
        return self.tail - self.head + 1

    def print(self):
        print(self.data)
        print("**********")
        print(self.data[self.head:self.tail])


class my_node:
    def __int__(self,data): # 构造函数
        self.data = data
        self.left = None
        self.right = None
        self.height = 1 # 高度，起始值

    # getter and setter
    def getdata(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getheight(self):
        return self.height

    def setdata(self,data):
        self.data = data
        return

    def setleft(self,node):
        self.left = node
        return

    def setright(self,node):
        self.right = node
        return

    def setheight(self,height):
        self.height = height


def getheight(node:my_node):
    if node is None:
        return 0
    return node.getheight()

def my_max(a,b):
    if a > b:
        return a
    return b

def rightrotate(node:my_node): #左边向右旋
#def leftrotate(node:my_node): #左边右旋
    print("left rotation node:", node.getdata())
    tmp = node.getleft() # 注意属性和方法
    node.setleft(tmp.getright())
    tmp.setright(node)

    h1 = my_max(getheight(node.getright()), getheight(node.getleft())) + 1 # 更新原节点层级，先看子树，再加一就是自己的高度
    node.setheight(h1) # 节点的左右子树，看那边的层级更高
    h2 = my_max(getheight(tmp.getright()), getheight(tmp.getleft())) + 1
    tmp.setheight(h2)

    return tmp

def leftrotate(node:my_node): #右边向左旋
#def leftrotate(node: my_node):  # 右边左旋
    print("right ratation node:", node.getdata())
    tmp = node.getright()
    node.setright(tmp.getleft())
    tmp.setleft(node)

    h1 = my_max(getheight(node.getright()), getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(tmp.getright()), getheight(tmp.getleft())) + 1
    tmp.setheight(h2)

    return tmp


def lrrotation(node:my_node): # 左右型-> 先左旋，再右旋
    node.setleft(leftrotate(node.getleft()))
    return rightrotate(node)


def rlrotation(node:my_node):
    node.setright(rightrotate(node.right()))
    return leftrotate(node)

'''
递归的精髓：
1)每个子问题处理好了，那么父问题就处理好了，每个子问题遵守规则了，那么父问题就遵守规则了
2)程序中类似node的变量不要总想着是最初识问题的变量，随着递归，node在不停的变化
3)递归程序要输入参数，并且一开始就要if判断终止条件，然后return值
4）程序分支流程中：到了终止条件的一定要return, 否则会一直None无限循环下去
'''
def insert_node(node,data):
    if node is None: # 根节点为空词，使用递归，一开始要判断退出条件
        return my_node(data) # 直接返回新建的根节点，一定要return

    if data < node.getdata(): # 左分支
        node.setleft(insert_node(node.getleft(), data)) # 这个递归很难理解，现在理解了，
        # 注意：由于上述递归，所以这里node视为当前最新节点的下下，只不过还需判断是右右还是右左类型
        if (getheight(node.getleft()) - getheight(node.getright()) == 2): #新元素插入到左边，可能导致数据不平衡
            if data < node.getleft().getdata():
                node = rightrotate(node) # 左左就右旋,返回新的根节点(node是递归中的节点)
            else:
                node = lrrotation(node)# 左右型

    else: # 右分支
        # 递归插到有分支
        node.setright(insert_node(node.getright(), data)) # 递归的精髓，如果属于root node的右边，继续执行一
        # 看看左右是否平衡，同理，如下递归中的子树业务对应查看是否平衡
        if getheight(node.getright()) - getheight(node.getleft())  == 2: # 新元素插入到右边，可能导致数据不平衡
            if data > node.getright().getdata(): #右右
                node = leftrotate(node)
            else:
                node = rlrotation(node)

    # 记得更新node的高度，还是站在当前node位置左右看看
    h1 =  my_max(getheight(node.getright()), getheight(node.getleft())) + 1
    node.setheight(h1)

    return node


def insert_data_self(node,data) ->my_node: # 插入到node节点下，新节点值为data，最终返回父node节点
    # 递归前判断终止条件
    if node is None:
        return my_node(data)

    # 开始递归插入
    if data < node.getdata():
        #insert_data_self(node.getleft(), data) # 递归插入左子树
        # 这个程序返回插入新元素后的主node，所以当前node下插入左边后，左边节点可能有变化
        node.setleft(insert_data_self(node.getleft(), data))
        if getheight(node.getleft()) - getheight(node.getright()) == 2: # 上述插入以后发生不平衡
            if data < node.getleft().getdata(): # 左左
                node = rightrotate(node) # 右旋，得到新的根节点，每个递归也是
            else:
                node = lrrotation(node) #左右型，先左旋，再右旋

    else:
        #insert_data_self(node.getright(),data)
        node.setright(insert_data_self(node.getright(), data))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            if data > node.getright().getdata():
                node = leftrotate(node)
            else:
                node = rlrotation(node)

    h1 = my_max(getheight(node.getlef()), getheight(node.getright())) + 1 # 记得要加1，因为还要包括本节点一层高度
    node.setheight(h1)

    return node


def getRightMost(root:my_node):
    while root:
        root = root.getright()
    return root.getdata()

def getLeftMost(root:my_node):
    while root:
        root = root.getleft()
    return root.getdata()


def del_node(root:my_node,data): # 从root的根节点开始删除一个元素值为data的节点
    if root.getdata() == data: #如果删除的是根节点，
        if root.getleft() is not None and root.getright() is not None:
            tmp_data = getLeftMost(root.getright()) # 从右节点的找最左节点，这个节点肯定比node.right要小，比左节点都大
            root.setdata(tmp_data) # 从新设置数据，关系都不用变，妙！加入为空咱么办？
            root.setright(del_node(root.getright(),tmp_data)) # 递归了，真他妈的妙！
        elif root.getleft() is not None:
            root = root.getleft() #更新根节点
        # 为什么这里没有return,因为相等的时候，相关节点已经置为None，等后面一起公用一个返回root
        else: # 当都为空时，效果和root.getright()一样都是置为空
            root = root.getright() #更新根节点

    elif root.getdata() > data: #左分支
        if root.getleft() is None: # 到底了，没查到，一定要记得返回
            print("no such data")
            # 如果不返回会怎么样？因为没找到，所以这里提前返回，后面的检查就都不用做啦！
            return root # 递归，前面要用到后面的返回，所以每次先判断到底的情况，记得返回
        else:
            root.setleft(del_node(root.getleft(),data))
    elif root.getdata() < data: #右分支
        if root.getright() is None:
            print("no such data")
            return root
        else:
            root.setright(del_node(root.getright(),data))

    if root is None:
        return root

    # 查看是否平衡
    if getheight(root.getleft()) - getheight(root.getright()) == 2:
        if getheight(root.getleft()) > getheight(root.getright()): #左左
            root = rightrotate(root)
        else:
            root = lrrotation(root)

    elif getheight(root.getleft()) - getheight(root.getright()) == -2:
        if getheight(root.getrigh()) > getheight(root.getleft()):
            root = leftrotate(root)
        else:
            root = rlrotation(root)

    height = my_max(getheight(root.getleft()), getheight(root.getright())) + 1
    root.setheight(height)

    return root #最终要返回根节点






class AVLtree:
    pass


if __name__ == "__main__":
    pass