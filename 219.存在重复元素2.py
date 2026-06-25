class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#第一反应是双重嵌套，这万万不可
#这涉及两个元素的判定关系，也许要哈希表
#首先，创建一个新字典来存储数据
#我觉得比较难的地方是条件判断的问题
#题目涉及了abs，是绝对值，但是呢我单向遍历，不用考虑
#我先把所有元素遍历一次
#因为条件是关于两个索引的，那我把value的位置给索引
#接下来判断索引关系就好了
#如果每一个不符合条件，就存在字典里面
#条件是，如果新的元素在字典里面，并且这个新元素的索引符合一定的条件，那么就返回
        dic = {}
        for i , a in enumerate(nums):
            if a in dic and i - dic[a] <= k:
                return True
            dic[a] = i
        return False

             
