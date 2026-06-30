class Solution:
    def isPalindrome(self, x: int) -> bool:
        left = 0
        right = len(str(x)) - 1
        #想到左右指针
        if x < 0:
            #负数一定不是回文数
            return False
        while True:
            #判断边界情况
            if left > right:
                break
            elif str(x)[right] == str(x)[left] :
                #这里不能使用int，要用字符串
                left += 1
                right -= 1
                #同时向中间逼近
            else:
                #不一样就不是
                return False
        #前面已经遍历完了，还没有输出就是回文数了   
        return True
    