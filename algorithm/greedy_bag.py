# 背小麦的贪婪问题，每种元素只有一个
def calc_profit(profit: list, weight: list, max_weight: int) -> int:
    """

    :param profit:
    :param weight:
    :param max_weight:
    :return:
    >>> calc_profit([1,2,3], [3,4,5],15)
    6
    >>> calc_profit([10,9,8],[3,4,5],25)
    27
    """

    if len(profit) != len(weight):
        raise ValueError("length doesn't math")
    if max_weight < 0:
        raise ValueError("max_weight must grater than zero")
    if any(p < 0 for p in profit):
        raise ValueError("profit cannot be negateive")
    if any(w < 0 for w in weight):
        raise ValueError("wegith cannot be negative")

    profit_by_weight = [p / w for p, w in zip(profit, weight)]  # 平局利润
    #print(profit_by_weight)

    sorted_profit_by_weight = sorted(profit_by_weight)
    #print(sorted_profit_by_weight)

    length = len(sorted_profit_by_weight)
    limit = 0 #当前已用重量
    gain = 0
    i = 0

    # 循环直到total weight 没有超过最大限制
    while limit <= max_weight and i < length:
        biggest_profit_by_weight = sorted_profit_by_weight[length - i - 1]  # 当前利润最大元素
        index = profit_by_weight.index(biggest_profit_by_weight) #利润最大的元素原来的索引位置
        profit_by_weight[index] = -1 #当前例如按最大元素已用，置为-1

        if max_weight - limit >= weight[index]: #如果当前利润最大的还未超重，继续使用
            limit += weight[index]
            gain += 1 * profit[index]
            print(gain)
        else: #如果当前元素超重，因为是背小麦wheat,所以可以按比例
            gain += (max_weight - limit) / weight[index] * profit[index]
            print(gain)
            break
        i += 1

    return gain


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print("input profits, weights, and max weight(all positive ints) separated by space.")
    # profit = [int(x) for x in input("input profile seperated by spaces: ").split()]
    # weight = [int(x) for x in input("input profile seperated by spaces: ").split()]
    # max_weight = int(input("max weight allow: "))
    #
    # calc_profit(profit, weight, max_weight)
