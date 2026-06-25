class Solution:
    def romanToInt(self, s: str) -> int:
        #我看了题解，这道题目的思路我觉得很新颖，是把字母结构改一改，分成
        #两个部分，一个是两个字母的减法，另一种是加法，把第一种挑出来
        #判断一下，直接加起来

        dic  = {"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        "IV":4,
        "IX":9,
        "XL":40,
        "XC":90,
        "CD":400,
        "CM":900,
        }
        #定义完了，接下来弄计数器和一份变量来存结果
        sums = 0
        i = 0
        #算法来了，这里使用while，方便更改i，用for不能更改i
        while i < len(s) :
            if s[i : i+2] in dic:
                sums += dic[s[i : i+2]]
                i += 2
            #如果是特殊结构就直接加，跳转到下两位
            else:
            #否则加当前位置的值，跳转到下一位
                sums += dic[s[i]]
                i += 1
        return sums

    