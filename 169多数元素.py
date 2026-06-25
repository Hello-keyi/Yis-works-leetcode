class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #对数组排序，取中间值
        nums = sorted(nums)
        #计算中间值
        a = len(nums) // 2
        #//是计算除法的整数部分
        return nums[a]