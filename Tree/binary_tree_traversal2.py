import queue

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def build_tree():
    print("\n***press n to stop entering at any point of time***\n")
    check = input("Enter the value of root node: ").strip().lower() or "n"
    if check == "n":
        return None

    q:queue.Queue = queue.Queue() #这里用来储存tree
    tree_node = TreeNode(int(check))
    q.put(tree_node)
    while not q.empty():
        node_found = q.get() # 队列中一次取得每个元素
        msg = "Enter the left node of %s: " % node_found.value
        check = input(msg).strip().lower() or "n"
        if check == "n":
            return tree_node
        left_node = TreeNode(int(check))
        node_found.left = left_node
        q.put(left_node)
        msg = "Enter the right node of %s: " % node_found.value
        check = input(msg).strip().lower() or  "n"
        if check == "n":
            return tree_node
        right_node = TreeNode(int(check))
        node_found.right = right_node
        q.put(right_node)


def pre_order(node:TreeNode) ->None:
    # 递归的思想：一开始就要判断不符合的条件然后执行返回，否则会错误
    if not node or not isinstance(node,TreeNode): # 如果为空或者不是TreeNode实例, 什么时候返回
        return

    print(node.value, end=" ")
    #if isinstance(node,TreeNode):
    #    print(node.value) # 没有返回条件，导致如下空对象继续执行
    pre_order(node.left)
    pre_order(node.right)

def middle_order(node:TreeNode) ->None:
    if not node or not isinstance(node,TreeNode):
        return
    middle_order(node.left)
    print(node.value, end=" ")
    middle_order(node.right)

def post_order(node:TreeNode) ->None:
    if not node or not isinstance(node,TreeNode):
        return
    post_order(node.left)
    post_order(node.right)
    print(node.value, end=" ")

def level_order(node:TreeNode) ->None:
    '''
    层级就不能递归了，只能队列
    :param node:
    :return:
    '''
    if not node or not isinstance(node,TreeNode):
        return
    q = queue.Queue()
    q.put(node)
    while not q.empty():
        current = q.get()
        print(current.value,end=" ")
        if current.left:
            q.put(current.left)
        if current.right:
            q.put(current.right)


def level_order_actual(node:TreeNode) ->None:
    if not node or not isinstance(node,TreeNode):
        return
    qone = queue.Queue() # 当前层的元素队列
    qtwo = queue.Queue() # 下一层的元素队列，额外的数据结构，也可以用list代替
    qone.put(node)
    while not qone.empty():
        current = qone.get()
        print(current.value, end=" ")
        if current.left:
            qtwo.put(current.left)
        if current.right:
            qtwo.put(current.right)
        if qone.empty(): # 当前层处理完成
            print("\n")  # 打印分隔符
            qone = qtwo  # 赋值qtwo到qone
            qtwo = queue.Queue() # 记得这事qtwo要清空

'''
python实现stack的3个数据结构
list:append替代push，pop弹出, 都是从后面
collections.deque
queue.LifoQueue
'''

'''
使用stack代替递归recursion
'''

def pre_order_iter(node:TreeNode) ->None:
   if not node or not isinstance(node,TreeNode):
       return
   stack = list() # 栈使用
   stack.append(node)
   while len(stack) > 0:
       current = stack.pop()
       print(current.value, end=" ")
       if current.right:
           stack.append(current.right)
       if current.left:
           stack.append(current.left)


def middle_order_iter(node:TreeNode) ->None:
    if not node or not isinstance(node,TreeNode):
        return
    stack = list() # 栈使用
    node = node
    while (node or stack):
        while (node):
            # print(node.value) #如果是前序
            stack.append(node)
            node = node.left # 先最左边一直到底
        node = stack.pop() # 刚开始弹出最左边元素
        print(node.value) # 中序，先打印左边元素
        node = node.right

def post_order_iter(node:TreeNode) ->None:
    if not node or not isinstance(node,TreeNode):
        return
    s1,s2 = [],[] # 需要两个栈
    current = node
    s1.append(current)

    while s1:
        current  = s1.pop()
        if current.left:
            s1.append(current.left)
        if current.right:
            s1.append(current.right)

        s2.append(current) # 第一个进去的最后出来


def length_node(node:TreeNode) ->int:
    if node is None:
        return 0
    #return lenght_node(node.left) + lenght_node(node.right) + 1
    ln = 1
    if node.left:
        ln += length_node(node.left)
    if node.right:
        ln += length_node(node.right)
    return ln

def traverse_inorder(node:TreeNode) ->None: # 代替return是一个yeild的生成器
    if not node or not isinstance(node,TreeNode):
        return
    if node.left:
        yield from traverse_inorder(node.left)
    yield node.value
    if node.right:
        yield from traverse_inorder(node.right) # 生成器

def max_height(node:TreeNode) ->int:
    if node is None:
        return 0
    if node.left:
        left_height = max_height(node.left) + 1
    else:
        left_height = 1
    if node.right:
        right_height = max_height(node.right) + 1
    else:
        right_height =1
    return max(left_height,right_height)

if __name__ == "__main__":
    node = build_tree()
    pre_order(node)
    print("\n")
    middle_order(node)
    print("\n")
    post_order(node)
    print("\n")
    level_order(node)
    print("\n")
    level_order_actual(node)
    print("\n")
    pre_order_iter(node)
    print("\nthe number nodes of tree is %d：" % (length_node(node)))
    #print("\nyields test\n")
    it = traverse_inorder(node)
    for i in it:print(i)
    print("\nmax tree height is %d: " % (max_height(node)))