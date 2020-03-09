#https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/red_black_tree.py
class RedBlackTree:
    def __init__(self,label=None,color=0,parent=None,left=None,right=None): # 0表示黑色，1表示红色
        self.label = label
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color


    def rotate_left(self):
        parent = self.parent
        right = self.right
        self.right = right.left
        if self.right: # 右节点调整
            self.right.left.parent  = self
        if parent is not None: # 父节点的子节点更新
            if parent.left == self:
                parent.left = right
            else:
                parent.right = right
        right.parent =  parent # 新的节点
        return right

    def rotate_right(self):
        parent = self.parent
        left = self.left
        self.left = left.right
        if self.left: # 如果没有当然就不会旋转啦，
            self.left.right.parent = self
        if parent is not None:
            if parent.left == self:
                parent.left = left
            else:
                parent.right = left
        left.parent = parent
        return left;


    def insert(self, label):
        if self.label is None:
            self.label = label
            return self
        if self.label == label:
            return self
        elif self.label > label:
            if self.left:
                self.insert(self.left,label)
            else:
                self.left = RedBlackTree(label,1,self) # 默认红色，父节点为self
                self.left._insert_repair() # 修复平衡
        else:
            if self.right:
                self.insert(self.right,label)
            else:
                self.right = RedBlackTree(label,1,self)
                self.right._insert_repair() # 修复平衡
        # 插入新节点后，需要平衡，这是有可能旋转(根节点不再是以前的了)，这时优先返回父节点，如果没有，返回自己
        return self.parent or self # 如果没有父节点，则返回自己？为什么要返回父节点？


    def _insert_repair(self):
        if self.parent is None:
            self.color=0 # 自己是根节点，必须设置颜色为黑色

        elif color(self.parent) == 0: #不是根节点，自己父节点为黑色
            self.color = 1 # 本节点为红色
        else:
            uncle = self.parent.sibing # 下面的@property 表示的get,set方法，这里相当于
            if color(uncle) == 0:
                pass


    def remove(self,label):
        if self.label == label:
            if self.left and self.right:
                value = self.left.get_max()
                self.label = value
                self.left.remove(value)



    @property # 属性，getter,setter
    def sibling(self):
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left


    def is_left(self):
        return self.parent and self.parent.left is self

    def is_right(self):
        return self.parent and self.parent.right is self

    def get_max(self): # 节点下最大的值
        # 方法一：不递归
        '''
        if not self.right: # 如果没有右节点
            return self.label
        while self.right is not None: #如果有就一直往下找
            self = self.right
        return self.label
        '''
        # 方法二：递归，因为依赖于一直往下查找
        if self.right:
            return self.right.get_max() # 本层输出依赖于下一层的输出，所以要return
        else:
            return self.label #到底了，直接返回最后的值


    def __bool__(self):
        return True

    def __len__(self): # 返回该树的节点数
        if self is None:
            return 0
        return self.__len__(self.left) + self.__len__(self.right) + 1



def color(node):
    if node is None:
        return 0
    else:
        return node.color