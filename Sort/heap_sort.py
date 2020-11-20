'''
堆排序：基于binary heap, 父节点index，左子节点是 2*index +1, 右子节点是2*index+2
    最大堆中最大数在root根节点，将最后一个元素和root元素交换，然后剩下n-1个元素形成一个最大堆，
    使用array/list表示这个heap
'''
def heapify(unsorted,index,heap_size):
    largest = index # 父节点在array中index位置
    left_index = 2 * index + 1 #左子节点
    right_index = 2 * index + 2 #右子节点
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index],unsorted[largest] #大的值放到根节点

        heapify(unsorted,largest,heap_size) #假如下面还设有更大的，继续往下

def heap_sort(unsorted):
    ln = len(unsorted)

    #构造一个max heap, 元素个数n,那么最下一个左子树开始，bottom-top构建一个max/min堆树
    for i in range( ln//2 -1, -1,-1):
        heapify(unsorted, i, ln)

    #逐个抽取最大元素(每个最大heap tree的根节点)
    for i in range(ln-1, 0, -1):
        # 最大值是根节点元素(index=0), 和最后一个元素交换位置，剩下再搞一个max heap tree
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted,0,i) # 剩下元素组成max heap tree
    return unsorted

if __name__ == "__main__":
    #user_input = input("enter numbers separated by a comma:\n").strip()
    #unsorted = [int(i) for i in user_input.split(",")]
    unsorted = [9,8,7,6,5,4,3,2,1]
    print(unsorted)
    print(heap_sort(unsorted))
