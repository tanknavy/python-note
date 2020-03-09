'''
广度优先算法：使用队列，同一层级（距离级别）优先遍历，
是不是和二叉树的层级访问很想，都是用队列

'''
def bfs(graph,start):
    explored,queue = set(),[start]
    explored.add(start)
    res = [start]
    while queue:
        v = queue.pop(0) # 取第一个元素
        #if v in explored:  #
        #    continue
        for w in graph[v]:
            if w not in explored: # 如果没有遍历过
                explored.add(w)
                res.append(w)
                queue.append(w)
    return res


def bfs2(graph,start):
    explored, queue = set(),[start]
    #explored.add(start)
    res = [start]
    while queue:
        v = queue.pop(0)
        # 为什么不能判断：下面使用队列，A->B,C：先A,再A的分支，再分支的分支
        #if v in explored:
        #    continue
        #explored.add(v) # 广度优先时，一个顶点所有的边先遍历
        #res.append(v)

        for w in graph[v]:
            if w not in explored:
                # 广度优先，直接先访问了
                explored.add(w)
                res.append(w)
                queue.append(w)
    return res

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(bfs(G,"A"))
print(bfs2(G,"A"))