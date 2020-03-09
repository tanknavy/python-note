def quick_sort(collection:list):
    ln = len(collection)
    if ln <=1:
        return collection
    else:
        pivot = collection.pop() # 当做栈，弹出最后一个元素作为参考元素
        left,right = [],[] # 这里没有原地调整循序排序
        for e in collection:
            if e < pivot:
                left.append(e)
            else:
                right.append(e)
        return quick_sort(left) + [pivot] + quick_sort(right) # 利用python的list可以直接合并


if __name__ == "__main__":
    #user_input = input("enter numbers separated by a comma:\n").strip()
    #unsorted = [int(i) for i in user_input.split(",")]
    unsorted = [9,8,7,6,5,4,3,2,1]
    print(unsorted)
    print(quick_sort(unsorted))