class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = []
        #先给一个列表，类似哈希表
        a = len(numbers) - 1
        #先给出左右索引值，这是大的
        b = 0
        #这是小的

        #给出无限循环，直到结果出现了为止
        while True:

            if numbers[b] + numbers[a] == target:
                #如果两数之和比较大，就把大索引减小，反之加大小索引，慢慢逼近目标
                l.append(b+1)
                l.append(a+1)
                #注意，答案要求加一位
                return l
            elif numbers[a] + numbers[b] < target:
                b += 1
            elif numbers[a] + numbers[b] > target:
                a -= 1
