class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        #给一个计数器，我直接枚举
        a = 0
        for i in patterns:
            if i in word:
                a += 1
        return a