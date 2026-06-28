class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        l = sorted(arr)
        i = 0
        #先排列，加上一个计数器
        if l[0] != 1:
            l[0] = 1
            #让第一个数字编程一
        while i <= len(l) - 1:
            if i == len(l) - 1:
                break
            #边界判断
            else:
                #判断绝对值大小，因为是有序排列，所以直接比较就可以
                if l[i] < l[i + 1]:
                    l[i+1] = l[i] + 1 
                i += 1
        #最后的数字就是最大的数字
        return l[i]