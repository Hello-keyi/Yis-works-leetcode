class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for j,i  in enumerate(nums):
            if i in dic:
                return True
            else:
                dic[i] = j
        return False
            