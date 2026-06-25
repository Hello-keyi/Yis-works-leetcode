class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
#这里使用哈希表
#这里学习新的函数方法 enumerate 这里第一个数字是索引，第二个数字是内容
#由于 a + b = b + a 我们只需要一个就好，先把一份放在字典里面，后面再来检验
        for j , x in enumerate(nums):
            need = target - x
            if need in dic:
                return [j,dic[need]]
            dic[x] = j