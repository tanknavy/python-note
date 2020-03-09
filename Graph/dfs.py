'''
深度优先算法：使用栈：对一个方向进行到底
'''
def dfs(graph,start):
    explored, stack = set(),[start] #已经遍历过的顶点，初始化一个栈
    res = []
    while stack:
        v = (stack.pop()) # pop默认弹出最后一个进入的Lifo，这里有括号还是代表元素而不是tuple
        #v = (stack.pop(0)) # 广度优先使用队列第一个
        # 如果不判断：可能会出现重复访问
        # A->B,C->弹出C,压入C的分支
        if v in explored: # 深度优先先要判断一下是否遍历过
            continue # 如果已经遍历过，直接进入下一轮循环

        explored.add(v) # 如果有遍历过，加入到遍历列表
        res.append(v)

        for w in graph[v]:
            if w not in explored: # 没有遍历过，把该元素相关的顶点放入栈中
                stack.append(w) # 加入即将遍历的栈中
    #return explored # 返回遍历结果
    return res


def dfs2(graph, start):
    explored, stack = set(),[start]
    res = []

    while stack:
        v = stack.pop() # pop默认是弹出最后一个
        # 只要是弹出来的，先看看这个节点是否被深度访问过
        if v in explored:
            continue

        explored.add(v)
        res.append(v)

        for w in graph[v]: # 深度遍历需要进栈
            if w not in explored: # 如果这个节点没有被遍历过，就进栈
                stack.append(w)

    #return explored # set是无序的，所以这个数据结果不正确
    return res # set是无序的，所以这个数据结果不正确


def bfs(graph, start):
    pass


# 图的map
G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(dfs(G,"A"))
print(dfs2(G,"A"))
