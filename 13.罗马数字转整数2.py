class Solution:
    def romanToInt(self, s: str) -> int:
        #这个解法是利用数值大小来判断
        #如果前面比后面的大或者等于，就加，否则就减少
        #先创建一个字典来存储数据
        dic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        sums = 0
        #这是一个存储答案的变量
        for i in range(len(s)):
            if i == len(s) -1 :
                #如果i是最大的数，就不比了
                sums += (dic[s[i]])
            elif dic[s[i]] >= dic[s[i+1]]:
                #如果i不是最大的数，判断是否前面比后面大
                sums += (dic[s[i]])
            else:
                ##如果i不是最大的数字并且前面的数字比后面小
                sums -= dic[s[i]]
        return sums



