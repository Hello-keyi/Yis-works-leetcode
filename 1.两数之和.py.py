class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for j , x in enumerate(nums):
            need = target - x
            if need in dic:
                return [j,dic[need]]
            dic[x] = j