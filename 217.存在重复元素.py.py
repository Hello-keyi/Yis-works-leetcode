class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
#先弄一个字典，方便后续存储数据
#这些题目的典型特点是，先用for 和enumerate遍历列表，然后用条件判断
# 不符合就塞在字典里，符合就return
        for j,i  in enumerate(nums):
            if i in dic:
                return True
            else:
                dic[i] = j
        return False
            