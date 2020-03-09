class TwoSum():
    def twosum1(self,nums:[],target:int) ->int:
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        map = {}
        #for (i=0;i<len(nums);i++):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        raise Exception("no solution for target")

    def twosum2(self, nums: [], target: int) -> int:
        pass

    def twosum3(self, nums: [], target: int) -> int:
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map.keys():
                return [i,map.get(complement)]
            map[nums[i]] = i
        raise Exception("no solution for target")

if __name__ == "__main__":
    arr = [2, 11, 15, 7]
    #arr = {1:2,2:11,3:15,4:7}
    target = 9
    #TwoSum()
    #print(TwoSum().twosum1(arr,target))#实例化对象
    print(TwoSum().twosum3(arr,target))  # 实例化对象