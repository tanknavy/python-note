'''
归并排序
'''

def merge_sort(collection):
    # 合并两个有序数组为一个并返回
    def merge(left,right):# 两个有序列表的合并依然是有序，为什么是有序的
        result = []
        while left and right: # 左右连个列表都不为空
            result.append((left if left[0] <= right[0] else right).pop(0)) # pop默认最后一个，这里第一个
        return result + left + right # 任何一个先为空，剩下的都为大于result里面的，有序列表

    # 递归终止条件，只有一个元素时返回
    if len(collection) <= 1:
        return collection

    # 要递归的数据分支，类似于二叉树的左右，
    mid = len(collection) // 2 # 商，整数类型
    # 想象成左右两个子树，两边都有序了，再合并起来
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))

if __name__ == "__main__":
    #user_input = input("enter numbers separated by a comma:\n").strip()
    #unsorted = [int(i) for i in user_input.split(",")]
    unsorted = [9,8,7,6,5,4,3,2,1]
    print(unsorted)
    print(merge_sort(unsorted))