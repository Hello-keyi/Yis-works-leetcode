class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#这是第一道我没看题解就写出来的题目，很开心
#这一道题是返回交集，我想着先弄一个列表，后面把交际元素塞进去，最后返回来
#我创建列表，判断nums1里面的东西是否符合条件，也就是是否在nums2里面
#接着，如果是，那么加进列表里面，如果不是，那么跳过
#最后输出列表，万事大吉
        a = []
        for i , j in enumerate(nums1):
            if j in nums2 and j not in a:
                a.append(j)
        return a
